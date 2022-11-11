from django.contrib import admin

from modeltranslation.admin import TranslationStackedInline, TranslationAdmin

from core import models, forms
from snippets.admin import BaseModelAdmin
from snippets.admin.multiupload import BaseMultipleFileUploadAdmin
from snippets.utils.modeltranslation import get_model_translation_fields


@admin.register(models.CallToAction)
class CallToActionAdmin(BaseModelAdmin, TranslationAdmin):
    """Призывы к действию"""

    fields = models.CallToAction().collect_fields()
    list_display = ('id', 'title', 'ordering', 'status', 'updated')
    list_display_links = ('id', 'title')
    list_filter = BaseModelAdmin.list_filter + ('button_order',)
    search_fields = ['=id'] + get_model_translation_fields(models.CallToAction)


class GalleryPhotoInline(TranslationStackedInline):
    """Фото галереи"""

    extra = 0
    fields = models.GalleryPhoto().collect_fields()
    model = models.GalleryPhoto
    readonly_fields = ('created', 'updated')


@admin.register(models.Gallery)
class GalleryAdmin(BaseMultipleFileUploadAdmin, BaseModelAdmin, TranslationAdmin):
    """Галереи"""

    fields = models.Gallery().collect_fields() + ['multiupload']
    form = forms.GalleryForm
    inline_photo_model = models.GalleryPhoto
    inlines = (GalleryPhotoInline,)
    list_display = ('image_thumb', 'title', 'ordering', 'status', 'updated')
    list_display_links = ('image_thumb', 'title')
    ordering = BaseModelAdmin.ordering + ('title',)
    photo_model_related_name = 'gallery'
    search_fields = ['=id'] + get_model_translation_fields(models.Gallery)


@admin.register(models.SubscribeBlock)
class SubscribeBlockAdmin(BaseModelAdmin, TranslationAdmin):
    """Блоки подписки"""

    fields = models.SubscribeBlock().collect_fields()
    list_display = ('id', 'title', 'ordering', 'status', 'updated')
    list_display_links = ('id', 'title')
    search_fields = ['=id'] + get_model_translation_fields(models.SubscribeBlock)
