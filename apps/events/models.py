from django.db import models

from ckeditor_uploader.fields import RichTextUploadingField

from snippets.models import BaseModel, BaseDictionaryModel
from snippets.models.image import ImageMixin
from snippets.models.pages import BasePage, HeroMixin
from snippets.models.seo import SEOModelMixin


class Event(HeroMixin, SEOModelMixin, ImageMixin, BaseModel):
    """Мероприятия"""

    title = models.CharField('Название', max_length=255)
    slug = models.SlugField(
        'Алиас', max_length=150, db_index=True, unique=True,
        help_text='Латинские буквы и цифры, подчеркивание и дефис'
    )
    list_image = models.ImageField(
        'Изображение в списке', upload_to='events/list', max_length=255,
        blank=True, null=True
    )
    excerpt = RichTextUploadingField(
        'Короткое описание',  blank=True, null=True
    )

    content_title = models.TextField(
        'Заголовок блока контента', max_length=4096, blank=True, null=True
    )
    client = models.CharField('Клиент', max_length=255, blank=True, null=True)
    categories = models.ManyToManyField(
        'events.EventCategory', verbose_name='Категории',
        related_name='events', blank=True
    )
    event_dates = models.CharField(
        'Даты мероприятия', max_length=255, blank=True, null=True
    )
    location = models.TextField(
        'Место проведения', max_length=1024, blank=True, null=True
    )
    content_1_subtitle = models.TextField(
        'Заголовок над контентом первой секции', max_length=1024, blank=True, null=True
    )
    content_1 = RichTextUploadingField('Контент первой секции', blank=True, null=True)
    gallery = models.ForeignKey(
        'core.Gallery', verbose_name='Галерея', on_delete=models.SET_NULL, blank=True, null=True
    )
    info_1_title = models.CharField(
        'Инфоблок, колонка 1: заголовок', max_length=255, blank=True, null=True
    )
    info_1_content = RichTextUploadingField('Инфоблок, колонка 1: контент', blank=True, null=True)
    info_2_title = models.CharField(
        'Инфоблок, колонка 2: заголовок', max_length=255, blank=True, null=True
    )
    info_2_content = RichTextUploadingField('Инфоблок, колонка 2: контент', blank=True, null=True)
    section_content = RichTextUploadingField('Контент жирным текстом', blank=True, null=True)
    content_2_subtitle = models.TextField('Подзаголовок второй секции', blank=True, null=True)
    content_2 = RichTextUploadingField('Контент второй секции', blank=True, null=True)
    content_2_image_1 = models.ImageField(
        'Вторая секция: изображение 1', upload_to='events/images', max_length=255, blank=True,
        null=True
    )
    content_2_image_2 = models.ImageField(
        'Вторая секция: изображение 2', upload_to='events/images', max_length=255, blank=True,
        null=True
    )
    content_2_image_3 = models.ImageField(
        'Вторая секция: изображение 3', upload_to='events/images', max_length=255, blank=True,
        null=True
    )
    show_call_to_action = models.BooleanField(
        'Показывать блок призыва к действию', default=True
    )
    call_to_action = models.ForeignKey(
        'core.CallToAction', on_delete=models.SET_NULL,
        verbose_name='Призыв к действию', blank=True, null=True,
        related_name='events'
    )
    allow_hero_title_from_title = False

    translation_fields = HeroMixin.translation_fields + SEOModelMixin.translation_fields + (
        'client', 'content_1', 'content_1_subtitle', 'content_2', 'content_2_image_1',
        'content_2_image_2', 'content_2_image_3', 'content_2_subtitle', 'content_title', 'excerpt',
        'info_1_content', 'info_1_title', 'info_2_content', 'info_2_title', 'list_image',
        'location', 'event_dates', 'section_content', 'title'
    )

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return f'/events/{self.slug}/'

    @property
    def categories_verbose(self):
        return ', '.join([x.title for x in self.categories.published()])


class EventIndicator(BaseModel):
    """Показатели мероприятия"""

    event = models.ForeignKey(
        'events.Event', verbose_name='Мероприятие', on_delete=models.CASCADE,
        related_name='indicators'
    )
    title = models.CharField('Заголовок', max_length=255)
    value = models.PositiveIntegerField('Значение', default=0)
    unit = models.CharField('Единица измерения', max_length=50, blank=True, null=True)

    translation_fields = ('title', 'unit')

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Показатель мероприятия'
        verbose_name_plural = 'Показатели мероприятия'

    def __str__(self):
        return self.title


class EventSectionIcon(ImageMixin, BaseModel):
    """Иконки секции контента мероприятия"""

    image_field = 'icon'
    event = models.ForeignKey(
        'events.Event', verbose_name='Мероприятие', on_delete=models.CASCADE,
        related_name='section_icons'
    )
    icon = models.FileField('Иконка', upload_to='events/icons', max_length=255)

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Иконка в контенте мероприятия'
        verbose_name_plural = 'Иконки в контенте мероприятия'

    def __str__(self):
        return str(self.id)


class EventCategory(BaseDictionaryModel):
    """Категории мероприятий"""

    slug = models.SlugField(
        'Алиас', max_length=150, db_index=True, unique=True,
        help_text='Латинские буквы и цифры, подчеркивание и дефис'
    )

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Категория мероприятий'
        verbose_name_plural = 'Категории мероприятий'


class EventsPage(BasePage):
    """Страница мероприятий"""

    event_button_caption = models.CharField(
        'Список мероприятий: текст кнопки "Подробнее"', max_length=255,
        blank=True, null=True
    )
    event_client_label = models.CharField(
        'Мероприятие: текст "Клиент"', max_length=255, blank=True, null=True
    )
    event_categories_label = models.CharField(
        'мероприятий: текст "Категории"', max_length=255, blank=True, null=True
    )
    event_date_label = models.CharField(
        'мероприятий: текст "Даты"', max_length=255, blank=True, null=True
    )
    location_label = models.CharField(
        'мероприятий: текст "Место проведения"', max_length=255, blank=True,
        null=True
    )

    show_call_to_action = models.BooleanField(
        'Показывать блок призыва к действию', default=True
    )
    call_to_action = models.OneToOneField(
        'core.CallToAction', on_delete=models.SET_NULL,
        verbose_name='Призыв к действию', blank=True, null=True
    )

    show_subscribe = models.BooleanField(
        'Показывать блок подписки', default=True
    )
    subscribe_block = models.OneToOneField(
        'core.SubscribeBlock', on_delete=models.SET_NULL,
        verbose_name='Блок подписки', blank=True, null=True
    )

    translation_fields = BasePage.translation_fields + (
        'location_label', 'event_button_caption', 'event_categories_label',
        'event_client_label', 'event_date_label'
    )

    class Meta:
        verbose_name = 'Страница мероприятий'
        verbose_name_plural = 'Страница мероприятий'

    def __str__(self):
        return 'Страница мероприятий'

    @staticmethod
    def get_absolute_url():
        return '/events/'
