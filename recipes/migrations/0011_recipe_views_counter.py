# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-27 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_recipe_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='views_counter',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
