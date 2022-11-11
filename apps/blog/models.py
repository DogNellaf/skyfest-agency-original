from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from snippets.models.articles import BaseArticle, BaseArticleSection
from snippets.models.pages import BasePage


class Article(BaseArticle):
    """Статья"""

    title = models.CharField('Заголовок', max_length=255, unique=True)
    slug = models.SlugField(
        'Алиас', max_length=150, db_index=True, unique=True,
        help_text='Латинские буквы и цифры, подчеркивание и дефис'
    )
    content = RichTextUploadingField('Контент', blank=True, null=True)
    show_on_home = models.BooleanField('Показывать на главной странице', default=True)

    translation_fields = BaseArticle.translation_fields + ('content',)

    class Meta:
        ordering = ('ordering', '-publish_date')
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/blog/{self.slug}/'


class ArticleSection(BaseArticleSection):
    """Секции статьи"""

    article = models.ForeignKey(
        'blog.Article', verbose_name='Статья', related_name='sections', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Секция статьи'
        verbose_name_plural = 'Секции статьи'


class BlogPage(BasePage):
    """Страница блога"""

    show_subscribe = models.BooleanField('Показывать блок подписки', default=True)
    subscribe_block = models.OneToOneField(
        'core.SubscribeBlock', on_delete=models.SET_NULL, verbose_name='Блок подписки',
        blank=True, null=True
    )

    translation_fields = BasePage.translation_fields

    class Meta:
        verbose_name = 'Страница блога'
        verbose_name_plural = 'Страница блога'

    def __str__(self):
        return 'Страница блога'

    @staticmethod
    def get_absolute_url():
        return '/blog/'
