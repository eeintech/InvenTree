# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-13 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_auto_20180412_0622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stocklocation',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]