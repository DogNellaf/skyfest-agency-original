from modeltranslation.decorators import register

from . import models
from snippets.utils.modeltranslation import BaseTranslationOptions


@register(models.Event)
class EventTranslationOptions(BaseTranslationOptions):
    fields = models.Event.translation_fields
    required_languages = {'default': ()}


@register(models.EventCategory)
class EventCategoryTranslationOptions(BaseTranslationOptions):
    fields = models.EventCategory.translation_fields
    required_languages = {'default': ()}


@register(models.EventIndicator)
class EventIndicatorTranslationOptions(BaseTranslationOptions):
    fields = models.EventIndicator.translation_fields
    required_languages = {'default': ()}


@register(models.EventsPage)
class EventsPageTranslationOptions(BaseTranslationOptions):
    fields = models.EventsPage.translation_fields
    required_languages = {'default': ()}
