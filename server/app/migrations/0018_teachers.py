# -*- coding: utf-8 -*-
import os
import re
import requests

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from django.db import migrations, models


base_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
        'avatars')

def save_image_from_file(field, name):
    path = os.path.join(base_path, name)
    f = open(path, 'rb')
    field.save(name, File(f), save=True)


def add_teacher(apps, schema_editor):
    Teacher = apps.get_model('app', 'Teacher')
    Profile = apps.get_model('app', 'Profile')
    Role = apps.get_model('app', 'Role')
    User = apps.get_model('auth', 'User')

    role = Role.objects.get(name='老师')
    for i in range(50):
        username = 'test%d' % i
        user = User.objects.get(username=username)
        if not hasattr(user, 'profile'):
            phone = '0000%d' % i
            profile = Profile(user=user, phone=phone, role=role)
            profile.gender = 'm' if i % 2 else 'f'
            name = 'img%d.jpg' % (i % 8)
            save_image_from_file(profile.avatar, name)
            profile.save()
            print(username)

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_users'),
    ]

    operations = [
        migrations.RunPython(add_teacher),
    ]
