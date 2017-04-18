# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 05:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quanly', '0027_auto_20170416_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='DongPhoi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngayDongPhoi', models.DateField(blank=True, default=datetime.datetime.now)),
                ('ngayNopTien', models.DateField(blank=True, default=datetime.datetime.now)),
                ('added', models.BooleanField(default=False)),
                ('tt', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quanly.ThongTin')),
            ],
        ),
    ]
