from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):
    name = 'homepage'
    verbose_name = 'Главная страница'
