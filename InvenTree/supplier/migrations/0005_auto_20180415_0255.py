# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-15 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0004_auto_20180414_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]