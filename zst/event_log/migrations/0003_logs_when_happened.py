# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 13:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_log', '0002_auto_20161027_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='when_happened',
            field=models.DateField(default='1980-01-01'),
        ),
    ]
