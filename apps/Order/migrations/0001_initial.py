# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-06 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]