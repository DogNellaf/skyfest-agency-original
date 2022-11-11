from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):
    name = 'core'
    verbose_name = 'Основное'

    def ready(self):
        from core import templatetags  # NOQA
