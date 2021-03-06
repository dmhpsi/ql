# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 17:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quanly', '0011_auto_20170323_1252'),
    ]

    operations = [
        migrations.CreateModel(
            name='TinhDichDoNgayCH',
            fields=[
                ('tt', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='quanly.ThongTin')),
                ('matDo', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('doDiDong', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
                ('hinhDang', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.AddField(
            model_name='phoi',
            name='soCryotop2',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='phoi',
            name='soCryotop3',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='phoi',
            name='soCryotop4',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='phoi',
            name='soCryotop5',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='phoi',
            name='soPhoiN2',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='phoi',
            name='soPhoiN3',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='phoi',
            name='soPhoiN4',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='phoi',
            name='soPhoiN5',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='phoi',
            name='tongSoPhoiChuyen',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='phoi',
            name='tongSoPhoiHuy',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='phoi',
            name='tongSoPhoiLuuTruLanh',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='phoi',
            name='tongSoPhoiTiepTucTheoDoi',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='thongtin',
            name='hienNoan',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='thongtin',
            name='hienTinhTrung',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='trung',
            name='batThuong',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='trung',
            name='nangNoan',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='trung',
            name='thoaiHoa',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='trung',
            name='thoaiHoaSauICSI',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='trung',
            name='tongSoTrung',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='trung',
            name='tongSoTrungICSI',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='trung',
            name='tongSoTrungTT',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='trung',
            name='truongThanh',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='trung',
            name='vo',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='truphoi',
            name='PESAMESA',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='truphoi',
            name='PICSI',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='truphoi',
            name='TESE',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='truphoi',
            name='truLanh',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='truphoi',
            name='truPhoiToanBo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='truphoi',
            name='xinTrung',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='phoi',
            name='loai1',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='phoi',
            name='loai2',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='phoi',
            name='loai3',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='trung',
            name='GV',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='trung',
            name='MI',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10000), django.core.validators.MinValueValidator(0)]),
        ),
    ]
