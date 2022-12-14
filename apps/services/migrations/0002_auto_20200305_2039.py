# Generated by Django 3.0.4 on 2020-03-05 17:39

import ckeditor_uploader.fields
import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200305_1630'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='excerpt',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1024, null=True, verbose_name='Короткое описание'),
        ),
        migrations.AddField(
            model_name='service',
            name='excerpt_en',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1024, null=True, verbose_name='Короткое описание'),
        ),
        migrations.AddField(
            model_name='service',
            name='excerpt_ru',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=1024, null=True, verbose_name='Короткое описание'),
        ),
        migrations.AddField(
            model_name='service',
            name='icon',
            field=models.FileField(blank=True, max_length=255, null=True, upload_to='services/icons', verbose_name='Иконка в списке'),
        ),
        migrations.CreateModel(
            name='ServicesPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('seo_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='META заголовок (title)')),
                ('seo_title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='META заголовок (title)')),
                ('seo_title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='META заголовок (title)')),
                ('seo_description', models.TextField(blank=True, max_length=1024, null=True, verbose_name='META описание (description)')),
                ('seo_description_ru', models.TextField(blank=True, max_length=1024, null=True, verbose_name='META описание (description)')),
                ('seo_description_en', models.TextField(blank=True, max_length=1024, null=True, verbose_name='META описание (description)')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('hero_subtitle', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Первый экран: Над заголовком')),
                ('hero_subtitle_ru', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Первый экран: Над заголовком')),
                ('hero_subtitle_en', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Первый экран: Над заголовком')),
                ('hero_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: заголовок')),
                ('hero_title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: заголовок')),
                ('hero_title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: заголовок')),
                ('hero_button_caption', models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: текст кнопки')),
                ('hero_button_caption_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: текст кнопки')),
                ('hero_button_caption_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: текст кнопки')),
                ('hero_button_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: ссылка кнопки')),
                ('hero_button_link_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: ссылка кнопки')),
                ('hero_button_link_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Первый экран: ссылка кнопки')),
                ('hero_bg_color', colorfield.fields.ColorField(default='#CCCCCC', max_length=18, verbose_name='Первый экран: цвет фона')),
                ('hero_bg', models.FileField(blank=True, max_length=255, null=True, upload_to='home/bg', verbose_name='Первый экран: изображение фона')),
                ('show_subscribe', models.BooleanField(default=True, verbose_name='Показывать блок подписки')),
                ('subscribe_block', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.SubscribeBlock', verbose_name='Блок подписки')),
            ],
            options={
                'verbose_name': 'Страница услуг',
                'verbose_name_plural': 'Страница услуг',
            },
        ),
    ]
