from django.db import models

from snippets.models import BaseModel
from snippets.models.image import ImageMixin


class Brand(ImageMixin, BaseModel):
    """Бренды"""

    image_field = 'logo'
    title = models.CharField('Заголовок', max_length=255)
    logo = models.FileField('Логотип', upload_to='home/brands', max_length=255)
    link = models.CharField('Сссылка', max_length=255, blank=True, null=True)

    translation_fields = ('link', 'logo', 'title')

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'

    def __str__(self):
        return self.title
