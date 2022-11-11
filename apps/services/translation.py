from modeltranslation.decorators import register

from services import models
from snippets.utils.modeltranslation import BaseTranslationOptions


@register(models.ServicesPage)
class ServicesPageTranslationOptions(BaseTranslationOptions):
    fields = models.ServicesPage.translation_fields
    required_languages = {'default': ()}


@register(models.Service)
class ServiceTranslationOptions(BaseTranslationOptions):
    fields = models.Service.translation_fields
    required_languages = {'default': ()}
