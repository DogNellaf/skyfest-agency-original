from modeltranslation.decorators import register

from about import models
from snippets.utils.modeltranslation import BaseTranslationOptions


@register(models.AboutEmployee)
class AboutEmployeeTranslationOptions(BaseTranslationOptions):
    fields = models.AboutEmployee.translation_fields
    required_languages = {'default': ()}


@register(models.AboutPage)
class AboutPageTranslationOptions(BaseTranslationOptions):
    fields = models.AboutPage.translation_fields
    required_languages = {'default': ()}
