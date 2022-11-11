from django.conf import settings
from django.db import models

from forms.choices import FormRequestReadStatusChoices
from snippets.models import LastModMixin, BasicModel, BaseModel


class BaseFormRequest(LastModMixin, BasicModel):
    """Base model for all request forms"""

    language = models.CharField(
        'Язык', max_length=6, default=settings.DEFAULT_LANGUAGE, choices=settings.LANGUAGES
    )
    read_status = models.SmallIntegerField(
        'Статус прочтение', choices=FormRequestReadStatusChoices.choices,
        default=FormRequestReadStatusChoices.UNREAD
    )

    email_fields = ('language',)

    class Meta:
        abstract = True


class Feedback(BaseFormRequest):
    """Обратная связь"""

    name = models.CharField('Имя', max_length=255, blank=True, null=True)
    phone_number = models.CharField('Телефон', max_length=18, blank=True, null=True)
    email = models.EmailField('Email', max_length=254, blank=True, null=True)
    comment = models.TextField('Сообщение', blank=True, null=True)
    url = models.CharField('Страница', max_length=255, blank=True, null=True)

    email_fields = BaseFormRequest.email_fields + (
        'name', 'phone_number', 'email', 'comment', 'url'
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Сообщение обратной связи'
        verbose_name_plural = 'Обратная связь'

    def __str__(self):
        return f'{self.name or ""} ({self.phone_number or "-"})'


class Order(BaseFormRequest):
    """Форма заказа"""

    name = models.CharField('Имя', max_length=255, blank=True, null=True)
    phone_number = models.CharField(
        'Телефон', max_length=18, blank=True, null=True
    )
    email = models.EmailField('Email', max_length=254, blank=True, null=True)
    role = models.ForeignKey(
        'vars.OrderRole', verbose_name='Роль', on_delete=models.SET_NULL,
        blank=True, null=True, related_name='orders'
    )
    comment = models.TextField('Сообщение', blank=True, null=True)
    url = models.CharField('Страница', max_length=255, blank=True, null=True)

    email_fields = BaseFormRequest.email_fields + (
        'name', 'phone_number', 'email', 'comment', 'url'
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.name or ""} ({self.phone_number or "-"})'


class Subscribe(BaseFormRequest):
    """Подписки"""

    email = models.EmailField('Email', max_length=254, unique=True)

    email_fields = BaseFormRequest.email_fields + ('email',)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'

    def __str__(self):
        return self.email
