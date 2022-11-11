from django.apps import AppConfig as BaseAppConfig


class AppConfig(BaseAppConfig):
    name = 'blog'
    verbose_name = 'Блог'
