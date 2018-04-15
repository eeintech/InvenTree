# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-15 01:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('track', '0003_auto_20180415_0147'),
    ]

    operations = [
        migrations.AddField(
            model_name='parttrackinginfo',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]