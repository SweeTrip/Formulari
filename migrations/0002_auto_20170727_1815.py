# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-27 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulari', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anagrafica',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='formulari',
            name='prez',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='produttori',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ripartizioni',
            name='note',
            field=models.TextField(null=True),
        ),
    ]