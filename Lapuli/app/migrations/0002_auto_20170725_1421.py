# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodmodel',
            name='description',
            field=models.CharField(max_length=2048),
        ),
    ]
