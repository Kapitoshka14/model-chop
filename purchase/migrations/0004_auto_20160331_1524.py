# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-31 10:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('purchase', '0003_auto_20160331_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='number',
            new_name='name',
        ),
    ]