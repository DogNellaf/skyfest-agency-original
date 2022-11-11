from django.contrib import admin

from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from solo.admin import SingletonModelAdmin

from . import models
from snippets.admin import BaseModelAdmin
from snippets.modeltranslation import get_model_translation_fields


@admin.register(models.EventCategory)
class EventCategoryAdmin(BaseModelAdmin, TranslationAdmin):
    """Категории мероприятий"""

    fields = models.EventCategory().collect_fields()
    list_display = ('title', 'slug', 'status', 'ordering', 'created')
    search_fields = ['id'] + get_model_translation_fields(models.EventCategory)

    class Media:
        js = ('admin/js/translit.js',)


class EventIndicatorInline(TranslationStackedInline):
    """Иконки секции мероприятия"""

    extra = 0
    fields = models.EventIndicator().collect_fields()
    model = models.EventIndicator
    readonly_fields = ('created', 'updated')
    suit_classes = 'suit-tab suit-tab-indicators'


class EventSectionIconInline(admin.TabularInline):
    """Иконки секции мероприятия"""

    extra = 0
    fields = models.EventSectionIcon().collect_fields()
    model = models.EventSectionIcon
    readonly_fields = ('created', 'updated')
    suit_classes = 'suit-tab suit-tab-info'


@admin.register(models.Event)
class EventAdmin(BaseModelAdmin, TranslationAdmin):
    """Мероприятия"""

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'title', 'slug', 'categories', 'list_image', 'excerpt',
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
            'classes': ('suit-tab', 'suit-tab-section_1'),
            'fields': (
                'content_title', 'client', 'event_dates', 'location',
                'content_1_subtitle', 'content_1', 'gallery'
            )
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info'),
            'fields': (
                'info_1_title', 'info_1_content', 'info_2_title',
                'info_2_content', 'section_content'
            )
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-section_2'),
            'fields': (
                'content_2_subtitle', 'content_2', 'content_2_image_1',
                'content_2_image_2', 'content_2_image_3'
            )
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-seo'),
            'fields': ('seo_title', 'seo_description')
        })
    )
    filter_horizontal = ('categories',)
    inlines = (EventSectionIconInline, EventIndicatorInline)
    list_display = ('title', 'slug', 'status', 'ordering', 'created')
    raw_id_fields = ('gallery',)
    search_fields = ['id'] + get_model_translation_fields(models.Event)
    suit_form_tabs = (
        ('general', 'Основное'),
        ('hero', 'Первый экран'),
        ('section_1', 'Секция №1'),
        ('info', 'Инфоблок'),
        ('indicators', 'Показатели'),
        ('section_2', 'Секция №2'),
        ('seo', 'SEO')
    )

    class Media:
        js = ('admin/js/translit.js',)


@admin.register(models.EventsPage)
class EventsPageAdmin(SingletonModelAdmin, TranslationAdmin):
    """Страница мероприятий"""

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ('title', 'event_button_caption', 'created', 'updated')
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
            'classes': ('suit-tab', 'suit-tab-event'),
            'fields': (
                'event_categories_label', 'event_client_label',
                'event_date_label', 'location_label'
            )
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
    readonly_fields = ('created', 'updated')
    suit_form_tabs = (
        ('general', 'Основное'),
        ('hero', 'Первый экран'),
        ('event', 'Отдельное мероприятие'),
        ('call_to_action', 'Призыв к действию'),
        ('subscribe', 'Подписка'),
        ('seo', 'SEO')
    )
