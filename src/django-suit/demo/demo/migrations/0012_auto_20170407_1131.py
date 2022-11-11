# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2017-04-07 08:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0011_auto_20170211_2156'),
    ]

    operations = [
        migrations.AddField(
            model_name='showcase',
            name='html5_color',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='html5_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='html5_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='showcase',
            name='country2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='showcase_country2_set', to='demo.Country', verbose_name=b'Django Select 2'),
        ),
    ]
