# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0016_auto_20180417_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockitemtracking',
            name='description',
        ),
        migrations.AddField(
            model_name='stockitemtracking',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]