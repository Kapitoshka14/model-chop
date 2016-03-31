# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-30 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50, verbose_name='Номер покупки')),
                ('status', models.BooleanField(default=False, verbose_name='Проплачена ли')),
                ('client', models.TextField(default='Будет вноситься через форму', verbose_name='Данные о покупателе')),
                ('body', models.TextField(verbose_name='Содержимое заказа')),
            ],
        ),
    ]
