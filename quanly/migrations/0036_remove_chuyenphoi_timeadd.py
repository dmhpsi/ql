# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-04 11:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quanly', '0035_auto_20170504_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chuyenphoi',
            name='timeAdd',
        ),
    ]