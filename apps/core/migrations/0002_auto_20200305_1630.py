# Generated by Django 3.0.4 on 2020-03-05 13:30

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CallToAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('ordering', models.IntegerField(db_index=True, default=0, verbose_name='Порядок')),
                ('status', models.SmallIntegerField(choices=[(0, 'Черновик'), (1, 'Публичный'), (2, 'Скрытый')], default=1, verbose_name='Статус')),
                ('bg_color', colorfield.fields.ColorField(default='#FFFFFF', max_length=18, verbose_name='Цвет фона')),
                ('bg', models.ImageField(blank=True, max_length=255, null=True, upload_to='call-to-action', verbose_name='Фон')),
                ('bg_ru', models.ImageField(blank=True, max_length=255, null=True, upload_to='call-to-action', verbose_name='Фон')),
                ('bg_en', models.ImageField(blank=True, max_length=255, null=True, upload_to='call-to-action', verbose_name='Фон')),
                ('subtitle', models.CharField(blank=True, max_length=255, null=True, verbose_name='Над заголовком')),
                ('subtitle_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Над заголовком')),
                ('subtitle_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Над заголовком')),
                ('title', models.TextField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('title_ru', models.TextField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('title_en', models.TextField(blank=True, max_length=255, null=True, verbose_name='Заголовок')),
                ('button_caption', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст кнопки')),
                ('button_caption_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст кнопки')),
                ('button_caption_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст кнопки')),
                ('button_link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка кнопки')),
                ('button_link_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка кнопки')),
                ('button_link_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Ссылка кнопки')),
            ],
            options={
                'verbose_name': 'Призыв к действию',
                'verbose_name_plural': 'Призывы к действию',
                'ordering': ('ordering',),
            },
        ),
        migrations.CreateModel(
            name='SubscribeBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('ordering', models.IntegerField(db_index=True, default=0, verbose_name='Порядок')),
                ('status', models.SmallIntegerField(choices=[(0, 'Черновик'), (1, 'Публичный'), (2, 'Скрытый')], default=1, verbose_name='Статус')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок формы')),
                ('title_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок формы')),
                ('title_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок формы')),
                ('button', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст кнопки')),
                ('button_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст кнопки')),
                ('button_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст кнопки')),
                ('bg', models.FileField(blank=True, max_length=255, null=True, upload_to='subscribe/bg', verbose_name='Фон')),
            ],
            options={
                'verbose_name': 'Блок подписки',
                'verbose_name_plural': 'Блоки подписки',
                'ordering': ('ordering',),
            },
        ),
        migrations.AlterModelOptions(
            name='galleryphoto',
            options={'ordering': ('ordering',), 'verbose_name': 'Фотография галереи', 'verbose_name_plural': 'Фотографии галереи'},
        ),
    ]