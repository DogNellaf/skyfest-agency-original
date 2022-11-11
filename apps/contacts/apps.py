from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):
    name = 'contacts'
    verbose_name = 'Контакты'
