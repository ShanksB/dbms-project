# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-14 08:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApplication', '0003_auto_20180414_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='BranchName',
            field=models.CharField(choices=[('cse', 'ComputerScience'), ('mech', 'MechanicalEngineering'), ('ece', 'ElectronicsAndCommunication')], max_length=10),
        ),
    ]
