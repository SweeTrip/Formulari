# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-27 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formulari', '0004_auto_20170827_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='prezzi',
            name='um',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='formulari.Um'),
        ),
    ]