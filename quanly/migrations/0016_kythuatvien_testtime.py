# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 03:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanly', '0015_kythuatvien'),
    ]

    operations = [
        migrations.AddField(
            model_name='kythuatvien',
            name='testTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]