# Generated by Django 3.0.4 on 2020-03-04 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfig',
            name='footer_logo',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='site_config/logos', verbose_name='Логотип для подвала (белый)'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='footer_logo_en',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='site_config/logos', verbose_name='Логотип для подвала (белый)'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='footer_logo_ru',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='site_config/logos', verbose_name='Логотип для подвала (белый)'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='logo',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='site_config/logos', verbose_name='Логотип'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='logo_en',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='site_config/logos', verbose_name='Логотип'),
        ),
        migrations.AddField(
            model_name='siteconfig',
            name='logo_ru',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='site_config/logos', verbose_name='Логотип'),
        ),
    ]
