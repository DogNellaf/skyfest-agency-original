from django.db import models
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField

from snippets.models import BaseModel
from snippets.models.abstract import ArticleManager
from snippets.models.image import ImageMixin
from snippets.models.pages import HeroMixin
from snippets.models.seo import SEOModelMixin


class BaseArticle(SEOModelMixin, HeroMixin, ImageMixin, BaseModel):
    """Базовая модель для статей и новостей"""

    title = models.CharField('Заголовок', max_length=255, db_index=True)
    slug = models.SlugField(
        'Алиас', max_length=150, db_index=True,
        help_text='Разрешены только латинские символы, цифры, символ подчеркивания и дефис (минус)'
    )
    publish_date = models.DateTimeField(
        'Дата публикации', db_index=True, default=timezone.now, help_text='Можно задать на будущее'
    )
    image = models.ImageField(
        'Изображение', upload_to='articles/%Y/%m/', max_length=255, blank=True, null=True
    )
    list_image = models.ImageField(
        'Изображение для анонса', upload_to='articles/list/%Y/%m/', max_length=255,
        blank=True, null=True
    )
    image_alt = models.CharField('Alt изображения', max_length=255, blank=True, null=True)

    translation_fields = HeroMixin.translation_fields + SEOModelMixin.translation_fields + (
        'image_alt', 'title'
    )
    objects = ArticleManager()

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class BaseArticleSection(BaseModel):
    """Базовый класс для секций статей"""

    title = models.CharField('Заголовок секции', max_length=255, blank=True, null=True)
    content = RichTextUploadingField('Контент', blank=True, null=True)
    gallery = models.ForeignKey(
        'core.Gallery', verbose_name='Галерея фотографий', blank=True, null=True,
        on_delete=models.SET_NULL
    )
    has_bg = models.BooleanField('С фоном', default=False)

    translation_fields = ('content', 'title')

    class Meta:
        abstract = True
        verbose_name = 'Секция статьи'
        verbose_name_plural = 'Секции статьи'

    def __str__(self):
        return str(self.pk) if self.pk else ''
