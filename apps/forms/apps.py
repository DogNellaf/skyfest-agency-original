from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):
    name = 'forms'
    verbose_name = 'Отправленные формы'
