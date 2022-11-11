from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from brands import models
from snippets.admin import BaseModelAdmin
from snippets.modeltranslation import get_model_translation_fields


@admin.register(models.Brand)
class BrandAdmin(BaseModelAdmin, TranslationAdmin):
    """Бренды"""

    fields = models.Brand().collect_fields()
    list_display = ('image_thumb', 'title', 'link', 'status', 'ordering', 'created')
    list_display_links = ('image_thumb', 'title')
    search_fields = ['id'] + get_model_translation_fields(models.Brand)
