from modeltranslation.decorators import register

from projects import models
from snippets.utils.modeltranslation import BaseTranslationOptions


@register(models.Project)
class ProjectTranslationOptions(BaseTranslationOptions):
    fields = models.Project.translation_fields
    required_languages = {'default': ()}


@register(models.ProjectCategory)
class ProjectCategoryTranslationOptions(BaseTranslationOptions):
    fields = models.ProjectCategory.translation_fields
    required_languages = {'default': ()}


@register(models.ProjectIndicator)
class ProjectIndicatorTranslationOptions(BaseTranslationOptions):
    fields = models.ProjectIndicator.translation_fields
    required_languages = {'default': ()}


@register(models.ProjectsPage)
class ProjectsPageTranslationOptions(BaseTranslationOptions):
    fields = models.ProjectsPage.translation_fields
    required_languages = {'default': ()}
