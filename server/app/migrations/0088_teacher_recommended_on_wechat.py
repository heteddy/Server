# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-24 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0087_auto_20160223_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='recommended_on_wechat',
            field=models.BooleanField(default=False),
        ),
    ]
