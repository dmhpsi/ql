# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanly', '0008_auto_20170323_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truphoi',
            name='maDongPhoi',
            field=models.CharField(default=b'-------', max_length=20),
        ),
    ]
