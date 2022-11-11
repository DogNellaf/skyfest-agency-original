# Generated by Django 3.0.4 on 2022-02-02 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20220203_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactspage',
            name='hero_button_content',
            field=models.TextField(blank=True, null=True, verbose_name='Первый экран: HTML-контент кнопки'),
        ),
        migrations.AddField(
            model_name='contactspage',
            name='hero_button_content_en',
            field=models.TextField(blank=True, null=True, verbose_name='Первый экран: HTML-контент кнопки'),
        ),
        migrations.AddField(
            model_name='contactspage',
            name='hero_button_content_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Первый экран: HTML-контент кнопки'),
        ),
        migrations.AlterField(
            model_name='contactspage',
            name='hero_button_script',
            field=models.TextField(blank=True, null=True, verbose_name='Первый экран: скрипт для кнопки'),
        ),
        migrations.AlterField(
            model_name='contactspage',
            name='hero_button_script_en',
            field=models.TextField(blank=True, null=True, verbose_name='Первый экран: скрипт для кнопки'),
        ),
        migrations.AlterField(
            model_name='contactspage',
            name='hero_button_script_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Первый экран: скрипт для кнопки'),
        ),
    ]
