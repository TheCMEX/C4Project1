# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_auto_20171124_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(default='Описание', max_length=250, verbose_name='Описание'),
        ),
    ]
