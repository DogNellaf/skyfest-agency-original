from django.db import models
from django.utils.translation import ugettext_lazy as _


class FormRequestReadStatusChoices(models.IntegerChoices):
    """Read status choices"""

    UNREAD = -1, _('Не прочитано')
    READ = 1, _('Прочитано')
