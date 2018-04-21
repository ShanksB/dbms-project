# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-21 12:18
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApplication', '0016_auto_20180421_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='feesnotification',
            name='HallTicketAvailable',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', max_length=5, validators=[django.core.validators.MinLengthValidator(4)]),
        ),
    ]
