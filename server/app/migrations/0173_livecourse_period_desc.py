# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-19 07:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0172_auto_20161018_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='livecourse',
            name='period_desc',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
