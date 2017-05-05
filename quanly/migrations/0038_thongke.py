# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-04 13:59
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quanly', '0037_chuyenphoi_timeadd'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThongKe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thang', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('nam', models.IntegerField(default=2017, validators=[django.core.validators.MinValueValidator(2017)])),
                ('tongSoTreSinh', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('tongSoTuiThai', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]