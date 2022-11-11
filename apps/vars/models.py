from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from solo.models import SingletonModel

from snippets.admin import SuperUserDeletableAdminMixin
from snippets.models import BaseModel, BasicModel
from vars.service import get_default_admins


class DbConfig(BaseModel):
    """Simple key-value storage in DB"""
    key = models.CharField('Ключ', max_length=250, db_index=True, unique=True)
    verbose_title = models.CharField('Что означает', max_length=250)
    value = models.TextField('Значение', blank=True)

    translation_fields = ('value',)

    class Meta:
        verbose_name = 'Переменная'
        verbose_name_plural = 'Переменные шаблонов'

    def __str__(self):
        return '%s (%s)' % (self.key, self.verbose_title)


class Menu(SuperUserDeletableAdminMixin, BaseModel):
    """Меню"""

    work_title = models.CharField('Рабочий заголовок', max_length=255, db_index=True)
    title = models.CharField('Заголовок', max_length=255, db_index=True, blank=True, null=True)
    slug = models.SlugField(
        'Алиас', db_index=True, unique=True,
        help_text='Латинские буквы и цифры, подчеркивание и дефис'
    )
    link = models.CharField('Ссылка', max_length=255, blank=True, null=True)
    translation_fields = ('link', 'title')

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.work_title


class MenuItem(SuperUserDeletableAdminMixin, BaseModel):
    """Пункт меню"""

    menu = models.ForeignKey(
        Menu, related_name='items', verbose_name='Меню', on_delete=models.CASCADE
    )
    title = models.CharField('Заголовок', max_length=255)
    url = models.CharField('Ссылка', max_length=255)
    class_name = models.CharField(
        'CSS-класс для ссылки (а):', blank=True, null=True, max_length=50
    )

    translation_fields = ('title', 'url')

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def __str__(self):
        return f'{self.menu}: {self.title}'


class OrderRole(BaseModel):
    """Роли в заказах"""

    title = models.CharField('Название', max_length=255)
    translation_fields = ('title',)

    class Meta:
        ordering = ('ordering',)
        verbose_name = 'Роль в заказе'
        verbose_name_plural = 'Роли в заказах'

    def __str__(self):
        return self.title


class SiteConfig(SingletonModel, BasicModel):
    """Настройки сайта"""

    admins = models.TextField(
        'Администраторы сайта', default=get_default_admins,
        help_text='через запятую, без пробелов'
    )
    logo = models.FileField(
        'Логотип', upload_to='site_config/logos', max_length=255, blank=True,
        null=True
    )
    footer_logo = models.FileField(
        'Логотип для подвала (белый)', upload_to='site_config/logos',
        max_length=255, blank=True,
        null=True
    )
    footer_slogan = RichTextUploadingField(
        'Подвал: текст под логотипом', blank=True, null=True
    )
    footer_contacts_title = models.CharField(
        'Подвал: заголовок колонки контактов', max_length=100, blank=True,
        null=True
    )

    address = models.TextField('Адрес', max_length=1024, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=100, blank=True, null=True)
    phone_2 = models.CharField(
        'Телефон 2', max_length=100, blank=True, null=True
    )
    public_email = models.EmailField(
        'Публичный email', max_length=254, blank=True, null=True
    )
    copyrights = models.TextField('Копирайт', blank=True, null=True)
    subscribe_title = models.CharField(
        'Заголовок блока подписки', max_length=255, blank=True, null=True
    )
    agree_text = models.CharField(
        'Текст соглашения о конфиденциальности под формой', max_length=255,
        blank=True, null=True
    )

    order_form_icon = models.FileField(
        'Форма заказа: иконка', upload_to='contacts/icons', max_length=255,
        blank=True, null=True
    )
    order_form_subtitle = models.CharField(
        'Форма заказа: подзаголовок', max_length=255, blank=True, null=True
    )
    order_form_title = models.TextField(
        'Форма заказа: заголовок', max_length=255, blank=True, null=True
    )
    order_form_name_label = models.CharField(
        'Форма заказа: ярлык поля имени', max_length=255, blank=True, null=True
    )
    order_form_email_label = models.CharField(
        'Форма заказа: ярлык поля email', max_length=255, blank=True, null=True
    )
    order_form_phone_label = models.CharField(
        'Форма заказа: ярлык поля телефона', max_length=255, blank=True,
        null=True
    )
    order_form_role_label = models.CharField(
        'Форма заказа: ярлык поля роли', max_length=255, blank=True, null=True
    )
    order_form_message_label = models.CharField(
        'Форма заказа: ярлык поля сообщения', max_length=255, blank=True,
        null=True
    )
    order_form_button_caption = models.CharField(
        'Форма заказа: текст кнопки', max_length=255, blank=True, null=True
    )

    translation_fields = (
        'address', 'agree_text', 'copyrights', 'footer_contacts_title',
        'footer_logo', 'footer_slogan', 'logo', 'order_form_button_caption',
        'order_form_email_label', 'order_form_message_label',
        'order_form_name_label', 'order_form_phone_label',
        'order_form_role_label', 'order_form_subtitle', 'order_form_title',
        'phone', 'phone_2', 'public_email', 'subscribe_title'
    )

    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    def __str__(self):
        return 'Настройки сайта'

    @staticmethod
    def get_order_roles():
        return OrderRole.objects.published()
