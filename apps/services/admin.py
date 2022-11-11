from django.contrib import admin

from modeltranslation.admin import TranslationAdmin
from solo.admin import SingletonModelAdmin

from services import models
from snippets.admin import BaseModelAdmin
from snippets.modeltranslation import get_model_translation_fields


@admin.register(models.Service)
class ServiceAdmin(BaseModelAdmin, TranslationAdmin):
    """Услуги"""

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'title', 'slug', 'icon', 'excerpt', 'projects',
                'show_call_to_action', 'call_to_action', 'status', 'ordering',
                'created', 'updated'
            )
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
            'classes': ('suit-tab', 'suit-tab-download'),
            'fields': (
                'show_download_block', 'download_file', 'download_icon', 'download_title',
                'download_description', 'download_button_caption'
            )
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-about'),
            'fields': ('about_image', 'about_title', 'about_content', 'about_content_colored')
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-seo'),
            'fields': ('seo_title', 'seo_description')
        })
    )
    filter_horizontal = ('projects',)
    list_display = ('image_thumb', 'title', 'slug', 'status', 'ordering', 'created')
    list_display_links = ('image_thumb', 'title')
    search_fields = ['id', 'slug'] + get_model_translation_fields(models.Service)
    suit_form_tabs = (
        ('general', 'Основное'),
        ('hero', 'Первый экран'),
        ('download', 'Скачивание'),
        ('about', 'Контент об услуге'),
        ('seo', 'SEO')
    )

    class Media:
        js = ('admin/js/translit.js',)


@admin.register(models.ServicesPage)
class ServicesPageAdmin(SingletonModelAdmin, TranslationAdmin):
    """Страница услуг"""

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'title', 'menu_title', 'service_button_caption', 'created',
                'updated'
            )
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
            'classes': ('suit-tab', 'suit-tab-content'),
            'fields': ('top_content', 'bottom_content')
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
    readonly_fields = ('created', 'updated')
    suit_form_tabs = (
        ('general', 'Основное'),
        ('hero', 'Первый экран'),
        ('content', 'Контент'),
        ('subscribe', 'Подписка'),
        ('seo', 'SEO')
    )
