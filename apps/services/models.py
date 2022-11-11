from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from snippets.models import BaseModel
from snippets.models.image import ImageMixin
from snippets.models.pages import BasePage, HeroMixin
from snippets.models.seo import SEOModelMixin


class ServicesPage(BasePage):
    """Страница услуг"""

    show_subscribe = models.BooleanField('Показывать блок подписки', default=True)
    subscribe_block = models.OneToOneField(
        'core.SubscribeBlock', on_delete=models.SET_NULL, verbose_name='Блок подписки',
        blank=True, null=True
    )
    service_button_caption = models.CharField(
        'Список услуг: текст кнопки "Подробнее"', max_length=255, blank=True, null=True
    )
    menu_title = models.CharField('Меню услуг: заголовок', max_length=255, blank=True, null=True)
    top_content = RichTextUploadingField(
        'Текст над списком услуг', blank=True, null=True
    )
    bottom_content = RichTextUploadingField(
        'Текст под списком услуг', blank=True, null=True
    )

    translation_fields = BasePage.translation_fields + (
        'bottom_content', 'menu_title', 'service_button_caption', 'top_content'
    )

    class Meta:
        verbose_name = 'Страница услуг'
        verbose_name_plural = 'Страница услуг'

    def __str__(self):
        return 'Страница услуг'

    @staticmethod
    def get_absolute_url():
        return '/services/'


class Service(ImageMixin, HeroMixin, SEOModelMixin, BaseModel):
    """Услуга"""

    image_field = 'icon'
    title = models.CharField('Название', max_length=255)
    slug = models.SlugField(
        'Алиас', max_length=150, db_index=True, unique=True,
        help_text='Латинские буквы и цифры, подчеркивание и дефис'
    )
    icon = models.FileField(
        'Иконка в списке', upload_to='services/icons', max_length=255, blank=True, null=True
    )
    excerpt = RichTextUploadingField('Короткое описание', max_length=1024, blank=True, null=True)

    show_download_block = models.BooleanField('Показывать блок скачивания', default=True)
    download_file = models.FileField(
        'Скачивание: файл', upload_to='services/downloads/files', max_length=255,
        blank=True, null=True
    )
    download_icon = models.FileField(
        'Скачивание: иконка файла', upload_to='services/downloads', max_length=255, blank=True,
        null=True
    )
    download_title = models.CharField(
        'Скачивание: заголовок блока', max_length=255, blank=True, null=True
    )
    download_description = RichTextUploadingField(
        'Скачивание: описание', max_length=1024, blank=True, null=True
    )
    download_button_caption = models.CharField(
        'Скачивание: текст кнопки', max_length=255, blank=True, null=True
    )

    about_image = models.ImageField(
        'Об услуге: изображение', upload_to='services/about', max_length=255, blank=True, null=True
    )
    about_title = models.CharField('Об услуге: заголовок', max_length=255, blank=True, null=True)
    about_content = RichTextUploadingField('Об услуге: описание', blank=True, null=True)
    about_content_colored = RichTextUploadingField(
        'Об услуге: описание с фоном', blank=True, null=True
    )

    projects = models.ManyToManyField('projects.Project', verbose_name='Проекты', blank=True)
    show_call_to_action = models.BooleanField(
        'Показывать блок призыва к действию', default=True
    )
    call_to_action = models.ForeignKey(
        'core.CallToAction', on_delete=models.SET_NULL,
        verbose_name='Призыв к действию', blank=True, null=True,
        related_name='services'
    )

    translation_fields = HeroMixin.translation_fields + (
        'about_content', 'about_content_colored', 'about_image', 'about_title',
        'download_button_caption', 'download_description', 'download_file', 'download_title',
        'excerpt', 'title'
    )

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return f'/services/{self.slug}/'
