# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-25 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anagrafica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('riferimento', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=200)),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Formulari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=200)),
                ('data', models.DateTimeField(blank=True, null=True)),
                ('um', models.CharField(max_length=2)),
                ('comm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulari.Anagrafica')),
            ],
        ),
        migrations.CreateModel(
            name='Materiali',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mat', models.CharField(max_length=200)),
                ('cod', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Prezzi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valore', models.CharField(max_length=200)),
                ('um', models.CharField(max_length=2)),
                ('data', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField()),
                ('comm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulari.Anagrafica')),
                ('mat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulari.Materiali')),
            ],
        ),
        migrations.CreateModel(
            name='Produttori',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('riferimento', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=200)),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ripartizioni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('mail', models.CharField(max_length=200)),
                ('riferimento', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=200)),
                ('note', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='formulari',
            name='prez',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulari.Prezzi'),
        ),
        migrations.AddField(
            model_name='formulari',
            name='prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulari.Produttori'),
        ),
        migrations.AddField(
            model_name='formulari',
            name='ripa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formulari.Ripartizioni'),
        ),
    ]