# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-05 09:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulari', '0023_auto_20171205_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='anagrafica',
            name='addr',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]