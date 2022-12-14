# Generated by Django 3.0.4 on 2020-03-05 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
        ('homepage', '0003_auto_20200305_1943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeservice',
            name='content',
        ),
        migrations.RemoveField(
            model_name='homeservice',
            name='content_en',
        ),
        migrations.RemoveField(
            model_name='homeservice',
            name='content_ru',
        ),
        migrations.RemoveField(
            model_name='homeservice',
            name='image',
        ),
        migrations.RemoveField(
            model_name='homeservice',
            name='image_en',
        ),
        migrations.RemoveField(
            model_name='homeservice',
            name='image_ru',
        ),
        migrations.RemoveField(
            model_name='homeservice',
            name='title',
        ),
        migrations.RemoveField(
            model_name='homeservice',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='homeservice',
            name='title_ru',
        ),
        migrations.AddField(
            model_name='homepage',
            name='brands_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок брендов'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='brands_title_en',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок брендов'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='brands_title_ru',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Заголовок брендов'),
        ),
        migrations.CreateModel(
            name='HomeBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('ordering', models.IntegerField(db_index=True, default=0, verbose_name='Порядок')),
                ('status', models.SmallIntegerField(choices=[(0, 'Черновик'), (1, 'Публичный'), (2, 'Скрытый')], default=1, verbose_name='Статус')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='brands.Brand', verbose_name='Бренд')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='brands', to='homepage.HomePage', verbose_name='Страница')),
            ],
            options={
                'verbose_name': 'Услуга на главной',
                'verbose_name_plural': 'Услуги на главной',
                'ordering': ('ordering',),
            },
        ),
    ]
