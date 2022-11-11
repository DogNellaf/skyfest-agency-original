# Generated by Django 3.0.4 on 2020-03-04 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('language', models.CharField(choices=[('ru', 'Russian'), ('en', 'English')], default='ru', max_length=6, verbose_name='Язык')),
                ('read_status', models.SmallIntegerField(choices=[(-1, 'Не прочитано'), (1, 'Прочитано')], default=-1, verbose_name='Статус прочтение')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('phone_number', models.CharField(blank=True, max_length=18, null=True, verbose_name='Телефон')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Сообщение')),
                ('url', models.CharField(blank=True, max_length=255, null=True, verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Сообщение обратной связи',
                'verbose_name_plural': 'Обратная связь',
                'ordering': ('-created',),
            },
        ),
    ]
