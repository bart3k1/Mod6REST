# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-25 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='persons', through='movies.Role', to='movies.Person'),
        ),
    ]
