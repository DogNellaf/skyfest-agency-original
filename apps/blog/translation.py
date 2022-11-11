from modeltranslation.decorators import register

from blog import models
from snippets.utils.modeltranslation import BaseTranslationOptions


@register(models.Article)
class ArticleTranslationOptions(BaseTranslationOptions):
    fields = models.Article.translation_fields
    required_languages = {'default': ()}


@register(models.ArticleSection)
class ArticleSectionTranslationOptions(BaseTranslationOptions):
    fields = models.ArticleSection.translation_fields
    required_languages = {'default': ()}


@register(models.BlogPage)
class BlogPageTranslationOptions(BaseTranslationOptions):
    fields = models.BlogPage.translation_fields
    required_languages = {'default': ()}
