# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-11 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulari', '0012_auto_20170911_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulari',
            name='prez',
            field=models.FloatField(),
        ),
    ]