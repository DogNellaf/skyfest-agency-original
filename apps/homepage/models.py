from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField
from solo.models import SingletonModel

from snippets.models import BaseModel, LastModMixin, BasicModel
from snippets.models.image import ImageMixin
from snippets.models.pages import BasePage, HeroMixin
from snippets.models.seo import SEOModelMixin


class HomePage(SEOModelMixin, LastModMixin, SingletonModel, BasicModel):
    """Главная страница"""

    title = models.CharField(
        'Заголовок', max_length=255, blank=True, null=True
    )
    show_brands = models.BooleanField('Показывать блок брендов', default=True)
    brands_title = models.CharField(
        'Заголовок брендов', max_length=255, blank=True, null=True
    )

    show_info_1 = models.BooleanField('Показывать инфоблок 1', default=True)
    info_1_subtitle = RichTextUploadingField(
        'Инфоблок 1: над заголовком', max_length=1024, blank=True, null=True
    )
    info_1_title = models.TextField(
        'Инфоблок 1: заголовок', max_length=512, blank=True, null=True
    )
    info_1_content = RichTextUploadingField(
        'Инфоблок 1: контент', blank=True, null=True
    )
    info_1_icon_1 = models.FileField(
        'Инфоблок 1: иконка 1', upload_to='home/info/icons', max_length=255,
        blank=True, null=True
    )
    info_1_icon_2 = models.FileField(
        'Инфоблок 1: иконка 2', upload_to='home/info/icons', max_length=255,
        blank=True, null=True
    )
    info_1_icon_3 = models.FileField(
        'Инфоблок 1: иконка 3', upload_to='home/info/icons', max_length=255,
        blank=True, null=True
    )
    info_1_button_caption = models.CharField(
        'Инфоблок 1: текст кнопки', max_length=255, blank=True, null=True
    )
    info_1_button_link = models.CharField(
        'Инфоблок 1: ссылка кнопки', max_length=255, blank=True, null=True
    )
    info_1_image_1 = models.ImageField(
        'Инфоблок 1: изображение 1', upload_to='home/info/images',
        max_length=255, blank=True, null=True
    )
    info_1_image_2 = models.ImageField(
        'Инфоблок 1: изображение 2', upload_to='home/info/images',
        max_length=255, blank=True, null=True
    )

    show_projects = models.BooleanField(
        'Показывать блок анонсов проектов', default=True
    )
    show_services = models.BooleanField(
        'Показывать блок анонсов услуг', default=True
    )

    services_icon = models.FileField(
        'Услуги: иконка', upload_to='home/services/icons', max_length=255,
        blank=True, null=True
    )
    services_subtitle = RichTextUploadingField(
        'Услуги: над заголовком', max_length=1024, blank=True, null=True
    )
    services_title = models.TextField(
        'Услуги: заголовок', max_length=1024, blank=True, null=True
    )

    show_info_2 = models.BooleanField('Показывать инфоблок 2', default=True)
    info_2_subtitle = RichTextUploadingField(
        'Инфоблок 2: над заголовком', max_length=1024, blank=True, null=True
    )
    info_2_title = models.TextField(
        'Инфоблок 2: заголовок', max_length=512, blank=True, null=True
    )
    info_2_content = RichTextUploadingField(
        'Инфоблок 2: контент', blank=True, null=True
    )
    info_2_image = models.FileField(
        'Инфоблок 2: изображение под контентом', upload_to='home/info/images',
        max_length=255, blank=True, null=True
    )
    info_2_button_caption = models.CharField(
        'Инфоблок 2: текст кнопки', max_length=255, blank=True, null=True
    )
    info_2_button_link = models.CharField(
        'Инфоблок 2: ссылка кнопки', max_length=255, blank=True, null=True
    )
    info_2_image_1 = models.ImageField(
        'Инфоблок 2: изображение 1', upload_to='home/info/images',
        max_length=255, blank=True, null=True
    )
    info_2_image_2 = models.ImageField(
        'Инфоблок 2: изображение 2', upload_to='home/info/images',
        max_length=255, blank=True, null=True
    )
    info_2_image_3 = models.ImageField(
        'Инфоблок 2: изображение 3', upload_to='home/info/images',
        max_length=255, blank=True, null=True
    )

    show_info_3 = models.BooleanField('Показывать инфоблок 3', default=True)
    info_3_subtitle = RichTextUploadingField(
        'Инфоблок 3: над заголовком', max_length=1024, blank=True, null=True
    )
    info_3_title = models.TextField(
        'Инфоблок 3: заголовок', max_length=512, blank=True, null=True
    )
    info_3_content = RichTextUploadingField(
        'Инфоблок 3: контент', blank=True, null=True
    )
    info_3_icon_1 = models.FileField(
        'Инфоблок 3: иконка 1', upload_to='home/info/icons', max_length=255,
        blank=True, null=True
    )
    info_3_icon_2 = models.FileField(
        'Инфоблок 3: иконка 2', upload_to='home/info/icons', max_length=255,
        blank=True, null=True
    )
    info_3_icon_3 = models.FileField(
        'Инфоблок 3: иконка 3', upload_to='home/info/icons', max_length=255,
        blank=True, null=True
    )
    info_3_button_caption = models.CharField(
        'Инфоблок 3: текст кнопки', max_length=255, blank=True, null=True
    )
    info_3_button_link = models.CharField(
        'Инфоблок 3: ссылка кнопки', max_length=255, blank=True, null=True
    )
    info_3_image = models.ImageField(
        'Инфоблок 3: изображение справа', upload_to='home/info/images',
        max_length=255, blank=True, null=True
    )

    show_call_to_action = models.BooleanField(
        'Показывать блок призыва к действию', default=True
    )
    call_to_action = models.OneToOneField(
        'core.CallToAction', on_delete=models.SET_NULL,
        verbose_name='Призыв к действию', blank=True, null=True
    )

    show_blog = models.BooleanField('Показывать блок блога', default=True)
    blog_subtitle = RichTextUploadingField(
        'Блог: над заголовком', max_length=1024, blank=True, null=True
    )
    blog_title = models.CharField(
        'Блог: заголовок', max_length=255, blank=True, null=True
    )

    show_subscribe = models.BooleanField(
        'Показывать блок подписки', default=True
    )
    subscribe_block = models.OneToOneField(
        'core.SubscribeBlock', on_delete=models.SET_NULL,
        verbose_name='Блок подписки', blank=True, null=True
    )

    translation_fields = SEOModelMixin.translation_fields + (
        'blog_subtitle', 'blog_title', 'brands_title', 'info_1_button_caption',
        'info_1_button_link', 'info_1_content', 'info_1_image_1',
        'info_1_image_2', 'info_1_subtitle', 'info_1_title',
        'info_2_button_caption', 'info_2_button_link', 'info_2_content',
        'info_2_image', 'info_2_image_1', 'info_2_image_2', 'info_2_image_3',
        'info_2_subtitle', 'info_2_title', 'info_3_button_caption',
        'info_3_button_link', 'info_3_content', 'info_3_image',
        'info_3_subtitle', 'info_3_title', 'services_subtitle',
        'services_title', 'title'
    )

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'

    def __str__(self):
        return 'Главная страница'

    @staticmethod
    def get_absolute_url():
        return '/'


class HomeHeroSlide(HeroMixin, BaseModel):
    """Слайды первого экрана"""

    page = models.ForeignKey(
        'HomePage', related_name='slides', verbose_name='Страница',
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды первого экрана'


class HomeBrand(ImageMixin, BaseModel):
    """Бренды на главной"""

    page = models.ForeignKey(
        'homepage.HomePage', verbose_name='Страница', on_delete=models.CASCADE,
        related_name='brands'
    )
    brand = models.ForeignKey(
        'brands.Brand', verbose_name='Бренд', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Бренд на главной'
        verbose_name_plural = 'Бренды на главной'

    def __str__(self):
        return str(self.brand)


class HomeProject(ImageMixin, BaseModel):
    """Проекты на главной"""

    page = models.ForeignKey(
        'homepage.HomePage', verbose_name='Страница', on_delete=models.CASCADE,
        related_name='projects'
    )
    project = models.ForeignKey(
        'projects.Project', verbose_name='Проект', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Проект на главной'
        verbose_name_plural = 'Проекты на главной'

    def __str__(self):
        return str(self.project)


class HomeService(ImageMixin, BaseModel):
    """Услуги на главной"""

    page = models.ForeignKey(
        'homepage.HomePage', verbose_name='Страница', on_delete=models.CASCADE,
        related_name='services'
    )
    service = models.ForeignKey(
        'services.Service', verbose_name='Услуга', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Услуга на главной'
        verbose_name_plural = 'Услуги на главной'

    def __str__(self):
        return str(self.service)
