from django.contrib import admin

from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from solo.admin import SingletonModelAdmin

from about import models


class AboutEmployeeInline(TranslationStackedInline):
    """Команда"""

    extra = 0
    fields = models.AboutEmployee().collect_fields()
    model = models.AboutEmployee
    readonly_fields = ('created', 'updated')
    suit_classes = 'suit-tab suit-tab-team'


class AboutServiceInline(admin.TabularInline):
    """Услуги"""

    extra = 0
    fields = models.AboutService().collect_fields()
    model = models.AboutService
    readonly_fields = ('created', 'updated')
    suit_classes = 'suit-tab suit-tab-services'


@admin.register(models.AboutPage)
class AboutPageAdmin(SingletonModelAdmin, TranslationAdmin):
    """Страница о компании"""

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
            'classes': ('suit-tab', 'suit-tab-info_1'),
            'fields': (
                'show_info_1', 'info_1_subtitle', 'info_1_title', 'info_1_excerpt',
                'info_1_content_col_1', 'info_1_content_col_2', 'info_1_image'
            )
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-team'),
            'fields': ('show_team',)
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-services'),
            'fields': ('show_services',)
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-call_to_action'),
            'fields': ('show_call_to_action', 'call_to_action')
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
    inlines = (AboutEmployeeInline, AboutServiceInline)
    readonly_fields = ('created', 'updated')
    suit_form_tabs = (
        ('general', 'Основное'),
        ('hero', 'Первый экран'),
        ('info_1', 'Инфоблок 1'),
        ('team', 'Команда'),
        ('services', 'Услуги'),
        ('call_to_action', 'Призыв к действию'),
        ('subscribe', 'Подписка'),
        ('seo', 'SEO')
    )
