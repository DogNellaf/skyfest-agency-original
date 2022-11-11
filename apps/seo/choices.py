from django.db import models


class RedirectCodeChoices(models.IntegerChoices):
    """Location redirect codes"""

    C301 = 301, '301'
    C302 = 302, '302'
    C303 = 303, '303'
    C304 = 304, '304'
    C305 = 305, '305'
    C306 = 306, '306'
    C307 = 307, '307'
    C410 = 410, '410'
