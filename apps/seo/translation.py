from modeltranslation.decorators import register

from snippets.modeltranslation import BaseTranslationOptions
from seo import models


@register(models.SEOPage)
class SEOPageTranslationOptions(BaseTranslationOptions):
    fields = models.SEOPage.translation_fields
    required_languages = []
