# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 11:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanly', '0029_chochut_stt'),
    ]

    operations = [
        migrations.AddField(
            model_name='chuyenphoi',
            name='ngayRaPhoi',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]