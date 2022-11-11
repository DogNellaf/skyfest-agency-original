from django.contrib import admin

from modeltranslation.admin import TranslationStackedInline, TranslationAdmin
from solo.admin import SingletonModelAdmin

from snippets.admin import SuperUserDeletableAdminMixin, BaseModelAdmin
from snippets.utils.modeltranslation import get_model_translation_fields
from vars import models


@admin.register(models.DbConfig)
class DbConfigAdmin(SuperUserDeletableAdminMixin, BaseModelAdmin, TranslationAdmin):
    """Переменные шаблонов"""

    fields = models.DbConfig().collect_fields()
    list_display = ('key', 'verbose_title', 'status', 'created')
    list_editable = ('status',)
    ordering = ('key',)
    search_fields = ['=id', 'key', 'verbose_title'] + get_model_translation_fields(models.DbConfig)


class MenuItemInline(TranslationStackedInline):
    """Пункты меню"""

    extra = 0
    model = models.MenuItem
    fields = models.MenuItem().collect_fields()
    ordering = ('ordering',)
    readonly_fields = ('created', 'updated')
    suit_classes = 'suit-tab suit-tab-items'


@admin.register(models.Menu)
class MenuAdmin(SuperUserDeletableAdminMixin, BaseModelAdmin, TranslationAdmin):
    """Меню"""

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-basic'),
            'fields': models.Menu().collect_fields()
        })
    ]
    inlines = (MenuItemInline,)
    list_display = ('slug', 'work_title', 'title', 'status', 'created')
    list_editable = ('status',)
    ordering = BaseModelAdmin.ordering + ('slug',)
    search_fields = ['=id', 'link', 'slug', 'title', 'work_title'] + [
        'items__%s' % x for x in get_model_translation_fields(models.MenuItem)
    ]
    suit_form_tabs = (
        ('basic', 'Основное'),
        ('items', 'Пункты меню')
    )

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = tuple(self.readonly_fields)
        if request.user.is_superuser:
            return readonly_fields

        return readonly_fields + ('slug', 'work_title')


@admin.register(models.MenuItem)
class MenuItemAdmin(SuperUserDeletableAdminMixin, BaseModelAdmin, TranslationAdmin):
    """Пункты меню отдельной админкой"""

    list_display = ('id', 'title', 'menu', 'status', 'ordering', 'created')
    list_display_links = ('id', 'title')
    list_filter = BaseModelAdmin.list_filter + ('menu',)
    search_fields = ['=id'] + get_model_translation_fields(models.MenuItem)


@admin.register(models.OrderRole)
class OrderRoleAdmin(BaseModelAdmin, TranslationAdmin):
    """Роли в заказах"""

    fields = models.OrderRole().collect_fields()
    list_display = ('id', 'title', 'ordering', 'status', 'created')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


@admin.register(models.SiteConfig)
class SiteConfigAdmin(SingletonModelAdmin, TranslationAdmin):
    """Настройки сайта"""

    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-basic'),
            'fields': ('admins',)
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-contacts'),
            'fields': ('phone', 'phone_2', 'public_email', 'address')
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-header'),
            'fields': ('logo',)
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-footer'),
            'fields': (
                'copyrights', 'footer_logo', 'footer_slogan',
                'footer_contacts_title'
            )
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-forms'),
            'fields': ('subscribe_title', 'agree_text')
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-order_form'),
            'fields': (
                'order_form_icon', 'order_form_subtitle', 'order_form_title',
                'order_form_name_label', 'order_form_email_label',
                'order_form_phone_label', 'order_form_role_label',
                'order_form_message_label', 'order_form_button_caption'
            )
        })
    ]
    suit_form_tabs = (
        ('basic', 'Основное'),
        ('contacts', 'Контакты'),
        ('header', 'Шапка'),
        ('footer', 'Подвал'),
        ('forms', 'Формы'),
        ('order_form', 'Форма заказа')
    )
