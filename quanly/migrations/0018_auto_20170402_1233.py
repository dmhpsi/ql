# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 05:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quanly', '0017_auto_20170402_1013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='truphoi',
            old_name='maDongPhoi',
            new_name='viTriTruPhoi',
        ),
    ]
