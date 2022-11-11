from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from blog import models
from snippets.admin.articles import BaseArticleAdmin, BaseArticleSectionInline
from snippets.modeltranslation import get_model_translation_fields
from solo.admin import SingletonModelAdmin


class ArticleSectionInline(BaseArticleSectionInline):
    """Секции статьи"""

    fields = models.ArticleSection().collect_fields()
    model = models.ArticleSection


@admin.register(models.Article)
class ArticleAdmin(BaseArticleAdmin):
    """Статьи"""

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': (
                'title', 'slug', 'publish_date', 'show_on_home', 'image', 'image_alt', 'ordering',
                'status', 'created', 'updated'
            )
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-body'),
            'fields': ('content',)
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-seo'),
            'fields': ('seo_title', 'seo_description')
        })
    )
    inlines = (ArticleSectionInline,)
    save_as = True
    search_fields = ['=id', 'slug', 'image'] + get_model_translation_fields(models.Article)

    class Media:
        js = ('admin/js/translit.js',)


@admin.register(models.BlogPage)
class BlogPageAdmin(SingletonModelAdmin, TranslationAdmin):
    """Страница блога"""

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
        ('subscribe', 'Подписка'),
        ('seo', 'SEO')
    )
