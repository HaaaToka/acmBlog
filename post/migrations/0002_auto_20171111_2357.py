# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(editable=False, max_length=130, unique=True),
        ),
    ]
