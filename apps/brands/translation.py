from modeltranslation.decorators import register

from brands import models
from snippets.utils.modeltranslation import BaseTranslationOptions


@register(models.Brand)
class BrandTranslationOptions(BaseTranslationOptions):
    fields = models.Brand.translation_fields
    required_languages = {'default': ()}
