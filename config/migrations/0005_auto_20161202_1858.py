# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-02 18:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_auto_20161202_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='config',
            name='native_theme',
            field=models.CharField(choices=[('DEFAULT', 'Default'), ('STARBUCKS', 'Starbucks'), ('MM', 'M&M')], default='none', max_length=20),
        ),
    ]
