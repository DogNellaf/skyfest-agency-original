from django.conf import settings

from modeltranslation.translator import TranslationOptions


class BaseTranslationOptions(TranslationOptions):
    required_languages = (settings.DEFAULT_LANGUAGE,)
    fallback_languages = {'default': settings.LANGUAGE_CODES}
    empty_values = ''


def get_model_translation_fields(model, with_original_fields=True):
    """
    Получает список всех переводимых полей для модели
    :param model - модель, для которой ищутся переводимые поля
    :param with_original_fields - добавляет оригинальные поля переводов (fallback поля)
    """
    fields = []
    if with_original_fields:
        fields.extend(model.translation_fields)

    for language in settings.LANGUAGE_CODES:
        fields.extend('%s_%s' % (x, language) for x in model.translation_fields)

    return fields


def get_model_translation_suit_tabs(model):
    """
    Получает список языковых табов для вывода в карточке объекта
    """
    fields_maps = {x.attname: x.verbose_name for x in model._meta.fields}
    return (('general', 'Основное'),) + tuple(
        (x, fields_maps.get(x, x)) for x in model.translation_fields
    )
