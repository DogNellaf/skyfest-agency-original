from django.db import models
from django.utils import timezone

from ckeditor_uploader.fields import RichTextUploadingField
from colorfield.fields import ColorField

from snippets.models import BaseModel
from snippets.models.image import ImageMixin


class CallToAction(BaseModel):
    """Призывы к действию"""

    bg_color = ColorField('Цвет фона', default='#FFFFFF')
    bg = models.ImageField(
        'Фон', upload_to='call-to-action', max_length=255, blank=True, null=True
    )
    subtitle = models.CharField('Над заголовком', max_length=255, blank=True, null=True)
    title = models.TextField('Заголовок', max_length=255, blank=True, null=True)
    button_caption = models.CharField('Текст кнопки', max_length=255, blank=True, null=True)
    button_link = models.CharField('Ссылка кнопки', max_length=255, blank=True, null=True)
    button_order = models.BooleanField(
        'Кнопка открывает форму заказа', default=False
    )

    translation_fields = (
        'bg', 'button_caption', 'button_link', 'subtitle', 'title'
    )

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Призыв к действию'
        verbose_name_plural = 'Призывы к действию'

    def __str__(self):
        return self.title or str(self.id)


class Gallery(ImageMixin, BaseModel):
    """Галерея фотографий"""

    title = models.CharField(
        'Рабочее название', max_length=255, db_index=True,
        help_text='Для идентификации в административной части сайта'
    )
    publish_date = models.DateTimeField(
        'Дата публикации', db_index=True, default=timezone.now, help_text='Можно задать на будущее'
    )
    image = models.ImageField(
        'Фотография', upload_to='galleries/images', null=True, blank=True
    )

    translation_fields = ('title',)

    class Meta:
        verbose_name = 'Галерея фотографий'
        verbose_name_plural = 'Галереи фотографий'

    def __str__(self):
        return self.title


class GalleryPhoto(ImageMixin, BaseModel):
    """Фотографии галерей"""

    gallery = models.ForeignKey(
        'core.Gallery', verbose_name='Галерея', related_name='photos', on_delete=models.CASCADE
    )
    image = models.ImageField(
        'Фотография', upload_to='galleries/photos/%Y/%m/%d'
    )
    alt = models.CharField(
        'Текст вместо фото (alt)', blank=True, null=False, max_length=255
    )
    body = RichTextUploadingField(
        'Описание фото', blank=True, null=False
    )

    translation_fields = ('alt', 'body')

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Фотография галереи'
        verbose_name_plural = 'Фотографии галереи'

    def __str__(self):
        return self.alt if self.alt else str(self.pk)


class SubscribeBlock(BaseModel):
    """Блоки подписки"""

    title = models.CharField('Заголовок формы', max_length=255, blank=True, null=True)
    button = models.CharField('Текст кнопки', max_length=255, blank=True, null=True)
    bg = models.FileField(
        'Фон', max_length=255, upload_to='subscribe/bg', blank=True, null=True
    )

    translation_fields = ('button', 'title')

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Блок подписки'
        verbose_name_plural = 'Блоки подписки'

    def __str__(self):
        return self.title or str(self.id)
