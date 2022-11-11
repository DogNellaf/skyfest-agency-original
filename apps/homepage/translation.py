from modeltranslation.decorators import register

from homepage import models
from snippets.utils.modeltranslation import BaseTranslationOptions


@register(models.HomePage)
class HomePageTranslationOptions(BaseTranslationOptions):
    fields = models.HomePage.translation_fields
    required_languages = {'default': ()}


@register(models.HomeHeroSlide)
class HomeHeroSlideTranslationOptions(BaseTranslationOptions):
    fields = models.HomeHeroSlide.translation_fields
    required_languages = {'default': ()}
