# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanly', '0014_auto_20170325_2225'),
    ]

    operations = [
        migrations.CreateModel(
            name='KyThuatVien',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=20)),
                ('nghiHuu', models.BooleanField(default=False)),
            ],
        ),
    ]
