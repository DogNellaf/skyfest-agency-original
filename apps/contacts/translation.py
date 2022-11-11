from modeltranslation.decorators import register

from contacts import models
from snippets.utils.modeltranslation import BaseTranslationOptions


@register(models.ContactBlock)
class ContactBlockTranslationOptions(BaseTranslationOptions):
    fields = models.ContactBlock.translation_fields
    required_languages = {'default': ()}


@register(models.ContactsPage)
class ContactsPageTranslationOptions(BaseTranslationOptions):
    fields = models.ContactsPage.translation_fields
    required_languages = {'default': ()}
