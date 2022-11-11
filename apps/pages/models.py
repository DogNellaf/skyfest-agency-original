from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from snippets.models import BaseModel
from snippets.models.seo import SEOModelMixin


class FlatPage(SEOModelMixin, BaseModel):
    """Простая страница"""

    title = models.CharField('Заголовок', max_length=255, blank=False, null=True)
    slug = models.SlugField(
        'Алиас', max_length=150, db_index=True, unique=True,
        help_text='Латинские буквы и цифры, подчеркивание и дефис'
    )
    content = RichTextUploadingField('Контент', blank=True)

    translation_fields = SEOModelMixin.translation_fields + ('content', 'title')

    class Meta:
        ordering = ('ordering', 'title')
        verbose_name = 'Простая страница'
        verbose_name_plural = 'Простые страницы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.slug}/'
