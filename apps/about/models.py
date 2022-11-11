from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from snippets.models import BaseModel
from snippets.models.image import ImageMixin
from snippets.models.pages import BasePage


class AboutPage(BasePage):
    """Страница о компании"""

    show_info_1 = models.BooleanField('Показывать инфоблок 1', default=True)
    info_1_subtitle = RichTextUploadingField(
        'Инфоблок 1: над заголовком', max_length=1024, blank=True, null=True
    )
    info_1_title = models.TextField('Инфоблок 1: заголовок', max_length=255, blank=True, null=True)
    info_1_excerpt = RichTextUploadingField('Инфоблок 1: короткий текст', blank=True, null=True)
    info_1_content_col_1 = RichTextUploadingField(
        'Инфоблок 1: контент, колонка 1', blank=True, null=True
    )
    info_1_content_col_2 = RichTextUploadingField(
        'Инфоблок 1: контент, колонка 2', blank=True, null=True
    )
    info_1_image = models.ImageField(
        'Инфоблок 1: изображение 1', upload_to='home/info/images', max_length=255,
        blank=True, null=True
    )

    show_team = models.BooleanField('Показывать блок команды', default=True)
    show_services = models.BooleanField('Показывать блок анонса услуг', default=True)

    show_call_to_action = models.BooleanField('Показывать блок призыва к действию', default=True)
    call_to_action = models.OneToOneField(
        'core.CallToAction', on_delete=models.SET_NULL, verbose_name='Призыв к действию',
        blank=True, null=True
    )
    show_subscribe = models.BooleanField(
        'Показывать блок подписки', default=True
    )
    subscribe_block = models.OneToOneField(
        'core.SubscribeBlock', on_delete=models.SET_NULL,
        verbose_name='Блок подписки',
        blank=True, null=True
    )

    translation_fields = BasePage.translation_fields + (
        'info_1_content_col_1', 'info_1_content_col_2', 'info_1_excerpt', 'info_1_image',
        'info_1_subtitle', 'info_1_title'
    )

    class Meta:
        verbose_name = 'Страница о компании'
        verbose_name_plural = 'Страница о компании'

    def __str__(self):
        return 'Страница о компании'

    @staticmethod
    def get_absolute_url():
        return '/about/'


class AboutEmployee(ImageMixin, BaseModel):
    """Команда"""

    page = models.ForeignKey(
        'about.AboutPage', verbose_name='Страница', on_delete=models.CASCADE,
        related_name='employees'
    )
    image = models.ImageField('Фото', upload_to='about/employees', max_length=255)
    title = models.CharField('ФИО', max_length=255)
    position = models.CharField('Должность', max_length=255, blank=True, null=True)

    translation_fields = ('position', 'title')

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Команда'

    def __str__(self):
        return self.title


class AboutService(ImageMixin, BaseModel):
    """Услуги на странице "О компании\""""

    page = models.ForeignKey(
        'about.AboutPage', verbose_name='Страница', on_delete=models.CASCADE,
        related_name='services'
    )
    service = models.ForeignKey(
        'services.Service', verbose_name='Услуга', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Услуга на странице "О компании"'
        verbose_name_plural = 'Услуги на странице "О компании"'

    def __str__(self):
        return str(self.service)
