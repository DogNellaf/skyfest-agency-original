from modeltranslation.decorators import register

from core import models
from snippets.utils.modeltranslation import BaseTranslationOptions


@register(models.CallToAction)
class CallToActionTranslationOptions(BaseTranslationOptions):
    fields = models.CallToAction.translation_fields
    required_languages = {'default': ()}


@register(models.Gallery)
class GalleryTranslationOptions(BaseTranslationOptions):
    fields = models.Gallery.translation_fields
    required_languages = {'default': ()}


@register(models.GalleryPhoto)
class GalleryPhotoTranslationOptions(BaseTranslationOptions):
    fields = models.GalleryPhoto.translation_fields
    required_languages = {'default': ()}


@register(models.SubscribeBlock)
class SubscribeBlockTranslationOptions(BaseTranslationOptions):
    fields = models.SubscribeBlock.translation_fields
    required_languages = {'default': ()}
