# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-21 11:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApplication', '0012_auto_20180421_1521'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feesapplication',
            old_name='cvv',
            new_name='Cvv',
        ),
    ]