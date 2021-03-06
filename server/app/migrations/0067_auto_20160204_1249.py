# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 04:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0066_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='schools')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='school',
            name='class_seat',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='school',
            name='study_seat',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='transferred_from',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trans_to_set', to='app.TimeSlot'),
        ),
        migrations.AddField(
            model_name='schoolphoto',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.School'),
        ),
    ]
