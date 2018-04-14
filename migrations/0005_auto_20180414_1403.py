# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-14 08:33
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApplication', '0004_auto_20180414_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='EmailId',
            field=models.EmailField(default='default@email.com', max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='student',
            name='Password',
            field=models.CharField(default='mypassword', max_length=25, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]
