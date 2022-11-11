from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from pages import models
from snippets.admin import BaseModelAdmin
from snippets.utils.modeltranslation import get_model_translation_fields


@admin.register(models.FlatPage)
class FlatPageAdmin(BaseModelAdmin, TranslationAdmin):
    """Простые страницы"""

    fieldsets = (
        (None, {
            'classes': ('suit-tab', 'suit-tab-general'),
            'fields': ('title', 'slug', 'status', 'created', 'updated')
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-content'),
            'fields': ('content',)
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-seo'),
            'fields': ('seo_title', 'seo_description')
        })
    )
    list_display = ('id', 'title', 'status', 'created')
    list_display_links = ('id', 'title')
    list_editable = ('status',)
    search_fields = ['=id', 'slug'] + get_model_translation_fields(models.FlatPage)

    suit_form_tabs = (
        ('general', 'Основное'),
        ('content', 'Контент'),
        ('seo', 'SEO')
    )

    class Media:
        js = ('admin/js/translit.js',)
