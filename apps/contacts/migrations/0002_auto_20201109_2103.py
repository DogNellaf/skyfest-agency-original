# Generated by Django 3.0.4 on 2020-11-09 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactspage',
            name='form_subtitle',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Форма: подзаголовок'),
        ),
        migrations.AlterField(
            model_name='contactspage',
            name='form_subtitle_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Форма: подзаголовок'),
        ),
        migrations.AlterField(
            model_name='contactspage',
            name='form_subtitle_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Форма: подзаголовок'),
        ),
    ]
