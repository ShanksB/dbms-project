# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-21 07:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApplication', '0008_admin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='admin',
            old_name='password',
            new_name='Password',
        ),
    ]