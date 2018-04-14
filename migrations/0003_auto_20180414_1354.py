# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-14 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExamApplication', '0002_student_branchname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='BranchName',
            field=models.CharField(choices=[('empty', ''), ('cse', 'ComputerScience'), ('mech', 'MechanicalEngineering'), ('ece', 'ElectronicsAndCommunication')], max_length=10),
        ),
    ]