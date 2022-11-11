from django.db import models

from snippets.models import BaseModel
from snippets.models.image import ImageMixin
from snippets.models.pages import BasePage


class ContactsPage(BasePage):
    """Страница контактов"""

    show_map = models.BooleanField('Показывать карту', default=True)
    map_latitude = models.FloatField('Карта: широта', blank=True, null=True)
    map_longitude = models.FloatField('Карта: долгота', blank=True, null=True)
    map_altitude = models.PositiveSmallIntegerField('Карта: альтитуда карты', default=15)

    show_form = models.BooleanField('Показывать форму', default=True)
    form_icon = models.FileField(
        'Форма: иконка', upload_to='contacts/icons', max_length=255, blank=True, null=True
    )
    form_subtitle = models.CharField('Форма: подзаголовок', max_length=255, blank=True, null=True)
    form_title = models.TextField(
        'Форма: заголовок', max_length=255, blank=True, null=True
    )
    form_name_label = models.CharField(
        'Форма: ярлык поля имени', max_length=255, blank=True, null=True
    )
    form_email_label = models.CharField(
        'Форма: ярлык поля email', max_length=255, blank=True, null=True
    )
    form_phone_label = models.CharField(
        'Форма: ярлык поля телефона', max_length=255, blank=True, null=True
    )
    form_message_label = models.CharField(
        'Форма: ярлык поля сообщения', max_length=255, blank=True, null=True
    )
    form_button_caption = models.CharField(
        'Форма: текст кнопки', max_length=255, blank=True, null=True
    )

    show_subscribe = models.BooleanField('Показывать блок подписки', default=True)
    subscribe_block = models.OneToOneField(
        'core.SubscribeBlock', on_delete=models.SET_NULL, verbose_name='Блок подписки',
        blank=True, null=True
    )

    translation_fields = BasePage.translation_fields + (
        'form_button_caption', 'form_email_label', 'form_message_label', 'form_name_label',
        'form_phone_label', 'form_subtitle', 'form_title'
    )

    class Meta:
        verbose_name = 'Страница контактов'
        verbose_name_plural = 'Страница контактов'

    def __str__(self):
        return 'Страница контактов'

    @staticmethod
    def get_absolute_url():
        return '/contacts/'


class ContactBlock(ImageMixin, BaseModel):
    """Блоки контактов"""

    image_field = 'icon'
    page = models.ForeignKey(
        'contacts.ContactsPage', verbose_name='Страница', on_delete=models.CASCADE,
        related_name='contact_blocks'
    )
    icon = models.FileField(
        'Иконка', upload_to='contacts/icons', max_length=255, blank=True, null=True
    )
    line_1 = models.TextField('Строка 1', blank=True, null=True)
    line_2 = models.TextField('Строка 2', blank=True, null=True)

    translation_fields = ()

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Блок контактов'
        verbose_name_plural = 'Блоки контактов'
