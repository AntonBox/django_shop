# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-03-21 00:18
from __future__ import unicode_literals

import apps.catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_merge_20170306_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to=apps.catalog.models.get_image_path),
        ),
    ]
