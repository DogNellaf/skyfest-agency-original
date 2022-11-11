from django.db import models


class PaymentStatusChoices(models.IntegerChoices):
    """Статусы оплаты"""

    NOT_PAID = -1, 'Не оплачено'
    PAID = 1, 'Оплачено'


class StatusChoices(models.IntegerChoices):
    """
    Object publicity status enumerate
    """

    DRAFT = 0, 'Черновик'
    PUBLIC = 1, 'Публичный'
    HIDDEN = 2, 'Скрытый'
