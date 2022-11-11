from django.contrib import admin

from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from solo.admin import SingletonModelAdmin

from contacts import models


class ContactBlockInline(TranslationStackedInline):
    """Блок контактов"""

    extra = 0
    fields = models.ContactBlock().collect_fields()
    model = models.ContactBlock
    readonly_fields = ('created', 'updated')
    suit_classes = 'suit-tab suit-tab-blocks'


@admin.register(models.ContactsPage)
class ContactsPageAdmin(SingletonModelAdmin, TranslationAdmin):
    """Страница контактов"""

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ('title', 'created', 'updated')
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-hero'),
            'fields': (
                'hero_subtitle', 'hero_title', 'hero_button_caption',
                'hero_button_link', 'hero_button_script',
                'hero_button_content', 'hero_button_order', 'hero_bg_color',
                'hero_bg', 'hero_bg_mobile', 'hero_bg_opacity'
            )
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-map'),
            'fields': ('show_map', 'map_latitude', 'map_longitude', 'map_altitude')
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-form'),
            'fields': (
                'show_form', 'form_icon', 'form_subtitle', 'form_title', 'form_name_label',
                'form_email_label', 'form_phone_label', 'form_message_label', 'form_button_caption'
            )
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-subscribe'),
            'fields': ('show_subscribe', 'subscribe_block')
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-seo'),
            'fields': ('seo_title', 'seo_description')
        })
    )
    inlines = (ContactBlockInline,)
    readonly_fields = ('created', 'updated')
    suit_form_tabs = (
        ('general', 'Основное'),
        ('hero', 'Первый экран'),
        ('blocks', 'Блоки'),
        ('map', 'Карта'),
        ('form', 'Форма'),
        ('subscribe', 'Подписка'),
        ('seo', 'SEO')
    )
