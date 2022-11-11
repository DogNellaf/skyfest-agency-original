from django.db import models

from snippets.models import BaseModel, BaseManager
from seo.choices import RedirectCodeChoices


class SEOMixin(models.Model):
    """Базовый класс для SEO-параметров модели"""
    seo_title = models.CharField('SEO Заголовок (title)', max_length=254, blank=True, null=True)
    seo_description = models.TextField('META Description', blank=True, null=True)
    seo_keywords = models.TextField('META Keywords', blank=True, null=True)

    translation_fields = ('seo_title', 'seo_description', 'seo_keywords')

    def collect_fieldsets(self, extra_general=None):
        fields = self.collect_fields()
        if extra_general:
            fields += extra_general
        return [
            ('Основное', {
                'classes': ('suit-tab suit-tab-general',),
                'fields': fields
            }),
            ('SEO', {
                'classes': ('suit-tab suit-tab-seo',),
                'fields': ['seo_title', 'seo_description', 'seo_keywords']
            }),
        ]

    def apply_seo_params(self, request):
        request.seo_params = {
            'seo_title': self.seo_title,
            'seo_description': self.seo_description,
            'seo_keywords': self.seo_keywords,
        }
        return request

    class Meta:
        abstract = True


class SEOPage(SEOMixin, BaseModel):
    """SEO properties"""
    url = models.CharField(
        'Ссылка (URL)', max_length=255, blank=True, db_index=True, unique=True,
        help_text='Введите URL страницы, параметры которой хотите переопределить, '
                  'без указания домена и языка! Например, /about/'
    )

    def __str__(self):
        return '%s: %s' % (self.url, self.seo_title)

    class Meta:
        verbose_name = 'SEO параметр'
        verbose_name_plural = 'SEO параметры'


class Redirect(BaseModel):
    """Location redirects"""
    old_path = models.TextField('Откуда', max_length=1024, db_index=True, unique=True)
    new_path = models.TextField('Куда', max_length=1024)
    status_code = models.PositiveSmallIntegerField(
        'Статус', choices=RedirectCodeChoices.choices, default=RedirectCodeChoices.C301
    )
    objects = BaseManager()

    def save(self, *args, **kwargs):
        result = super(Redirect, self).save(*args, **kwargs)
        from seo.router import router
        router.index()
        return result

    def __str__(self):
        return '%s: %s => %s' % (
            dict(RedirectCodeChoices.choices)[self.status_code],
            self.old_path,
            self.new_path,
        )

    class Meta:
        verbose_name = 'Редирект'
        verbose_name_plural = 'Редиректы'


class Robot(BaseModel):
    """Робот для robots.txt"""
    title = models.CharField('Имя робота', max_length=254)
    host = models.CharField('Host', max_length=254, blank=True, null=True)
    crawl_delay = models.DecimalField(
        'Crawl-delay', blank=True, null=True, decimal_places=1, max_digits=5
    )
    objects = BaseManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Робот (User-agent)'
        verbose_name_plural = 'Robots.txt'


class RobotDisallow(BaseModel):
    """Строка запрета для робота"""
    robot = models.ForeignKey(
        'Robot', verbose_name='Робот', related_name='disallows', on_delete=models.CASCADE
    )
    url_pattern = models.CharField('Шаблон (ссылка)', max_length=254)
    objects = BaseManager()

    class Meta:
        verbose_name = 'Disallow'
        verbose_name_plural = 'Disallow (Запреты)'


class RobotAllow(BaseModel):
    """Строка разрешения для робота"""
    robot = models.ForeignKey(
        'Robot', verbose_name='Робот', related_name='allows', on_delete=models.CASCADE
    )
    url_pattern = models.CharField('Шаблон ссылки', max_length=254)
    objects = BaseManager()

    class Meta:
        verbose_name = 'Allow'
        verbose_name_plural = 'Allow (Разрешения)'


class RobotCleanparam(BaseModel):
    """Строка Clean-param для робота"""
    robot = models.ForeignKey(
        'Robot', verbose_name='Робот', related_name='clean_params', on_delete=models.CASCADE
    )
    params = models.CharField('Параметры', max_length=255)
    url_pattern = models.CharField('Шаблон ссылки', max_length=255)
    objects = BaseManager()

    class Meta:
        verbose_name = 'Clean-param'
        verbose_name_plural = 'Параметры Clean-param'


class RobotSitemap(BaseModel):
    """Строка Sitemap для робота"""
    robot = models.ForeignKey(
        'Robot', verbose_name='Робот', related_name='sitemaps', on_delete=models.CASCADE
    )
    url = models.CharField('Sitemap', max_length=254)
    objects = BaseManager()

    class Meta:
        verbose_name = 'Sitemap'
        verbose_name_plural = 'Sitemap (Карты сайта XML)'
