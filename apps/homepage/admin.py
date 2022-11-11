from django.contrib import admin

from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
from solo.admin import SingletonModelAdmin

from homepage import models


class HomeBrandInline(admin.TabularInline):
    """Бренды на главной"""

    extra = 0
    fields = models.HomeBrand().collect_fields()
    model = models.HomeBrand
    readonly_fields = ('created', 'updated')
    suit_classes = 'suit-tab suit-tab-brands'


class HomeProjectInline(admin.TabularInline):
    """Проекты на главной"""

    extra = 0
    fields = models.HomeProject().collect_fields()
    model = models.HomeProject
    readonly_fields = ('created', 'updated')
    suit_classes = 'suit-tab suit-tab-projects'


class HomeServiceInline(admin.TabularInline):
    """Услуги на главной"""

    extra = 0
    fields = models.HomeService().collect_fields()
    model = models.HomeService
    readonly_fields = ('created', 'updated')
    suit_classes = 'suit-tab suit-tab-services'


class HomeHeroSlideInline(TranslationStackedInline):
    """Слайды первого экрана на главной"""

    extra = 0
    fields = models.HomeHeroSlide().collect_fields()
    model = models.HomeHeroSlide
    readonly_fields = ('created', 'updated')
    suit_classes = 'suit-tab suit-tab-hero'


@admin.register(models.HomePage)
class HomePageAdmin(SingletonModelAdmin, TranslationAdmin):
    """Главная страница"""

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ('title', 'created', 'updated')
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-brands'),
            'fields': ('show_brands', 'brands_title')
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info_1'),
            'fields': (
                'show_info_1', 'info_1_subtitle', 'info_1_title',
                'info_1_content', 'info_1_icon_1', 'info_1_icon_2',
                'info_1_icon_3', 'info_1_button_caption', 'info_1_button_link',
                'info_1_image_1', 'info_1_image_2'
            )
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info_2'),
            'fields': (
                'show_info_2', 'info_2_subtitle', 'info_2_title',
                'info_2_content', 'info_2_image', 'info_2_button_caption',
                'info_2_button_link', 'info_2_image_1', 'info_2_image_2',
                'info_2_image_3'
            )
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-info_3'),
            'fields': (
                'show_info_3', 'info_3_subtitle', 'info_3_title',
                'info_3_content', 'info_3_icon_1', 'info_3_icon_2',
                'info_3_icon_3', 'info_3_button_caption', 'info_3_button_link',
                'info_3_image'
            )
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-projects'),
            'fields': ('show_projects',)
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-services'),
            'fields': (
                'show_services', 'services_icon', 'services_subtitle',
                'services_title'
            )
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-call_to_action'),
            'fields': ('show_call_to_action', 'call_to_action')
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-blog'),
            'fields': ('show_blog', 'blog_subtitle', 'blog_title')
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
    inlines = (
        HomeBrandInline, HomeProjectInline, HomeServiceInline,
        HomeHeroSlideInline
    )
    readonly_fields = ('created', 'updated')
    suit_form_tabs = (
        ('general', 'Основное'),
        ('hero', 'Первый экран'),
        ('brands', 'Бренды'),
        ('info_1', 'Инфоблок 1'),
        ('info_2', 'Инфоблок 2'),
        ('info_3', 'Инфоблок 3'),
        ('projects', 'Проекты'),
        ('services', 'Услуги'),
        ('call_to_action', 'Призыв к действию'),
        ('blog', 'Блог'),
        ('subscribe', 'Подписка'),
        ('seo', 'SEO')
    )
