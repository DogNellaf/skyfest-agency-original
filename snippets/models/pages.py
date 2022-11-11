from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from colorfield.fields import ColorField
from solo.models import SingletonModel

from snippets.models import BasicModel, LastModMixin
from snippets.models.seo import SEOModelMixin


class HeroMixin(models.Model):
    hero_subtitle = RichTextUploadingField(
        'Первый экран: Над заголовком', blank=True, null=True
    )
    hero_title = models.CharField(
        'Первый экран: заголовок', max_length=255, blank=True, null=True
    )
    hero_button_caption = models.CharField(
        'Первый экран: текст кнопки', max_length=255, blank=True, null=True
    )
    hero_button_link = models.CharField(
        'Первый экран: ссылка кнопки', max_length=255, blank=True, null=True
    )
    hero_button_order = models.BooleanField(
        'Первый экран: кнопка открывает форму заказа', default=False
    )
    hero_button_content = models.TextField(
        'Первый экран: HTML-контент кнопки', blank=True, null=True
    )
    hero_button_script = models.TextField(
        'Первый экран: скрипт для кнопки', blank=True, null=True
    )
    hero_bg_color = ColorField('Первый экран: цвет фона', default='#CCCCCC')
    hero_bg = models.FileField(
        'Первый экран: изображение фона', upload_to='home/bg', max_length=255,
        blank=True, null=True
    )
    hero_bg_mobile = models.FileField(
        'Первый экран: изображение фона (мобильные)', upload_to='home/bg',
        max_length=255, blank=True, null=True
    )
    hero_bg_opacity = models.FloatField(
        'Первый экран: прозрачность фонового изображения', default=0.1,
        help_text='больше - светлее'
    )
    allow_hero_title_from_title = True

    translation_fields = (
        'hero_button_caption', 'hero_button_content', 'hero_button_link',
        'hero_button_script', 'hero_subtitle', 'hero_title'
    )

    class Meta:
        abstract = True


class BasePage(
    SEOModelMixin, HeroMixin, LastModMixin, SingletonModel, BasicModel
):
    """Базовая модель страниц"""

    title = models.CharField(
        'Заголовок', max_length=255, blank=True, null=True
    )

    translation_fields = (
        SEOModelMixin.translation_fields +
        HeroMixin.translation_fields +
        ('title',)
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.title if self.title else ''
