from modeltranslation.decorators import register

from pages import models
from snippets.utils.modeltranslation import BaseTranslationOptions


@register(models.FlatPage)
class FlatPageTranslationOptions(BaseTranslationOptions):
    fields = models.FlatPage.translation_fields
    required_languages = {'default': ()}
