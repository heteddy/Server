# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-12 03:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0112_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]
