# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-01 12:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20180127_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='recipeimage',
            name='recipe_image',
            field=models.ImageField(upload_to='media/recipes/images/'),
        ),
    ]
