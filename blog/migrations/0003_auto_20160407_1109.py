# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-07 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160330_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.CharField(max_length=200),
        ),
    ]
