# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-04 11:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanly', '0036_remove_chuyenphoi_timeadd'),
    ]

    operations = [
        migrations.AddField(
            model_name='chuyenphoi',
            name='timeAdd',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
