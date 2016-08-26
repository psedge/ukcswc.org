# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-26 00:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasters', '0004_auto_20160821_0557'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='times',
            field=models.CharField(choices=[('10.30', '10:30'), ('11.00', '11:00'), ('11.30', '11:30'), ('12.00', '12:00'), ('12.30', '12:30'), ('13.00', '13:00'), ('13.30', '13:30'), ('14.00', '14:00'), ('14.30', '14:30')], default='11.30', max_length=255),
            preserve_default=False,
        ),
    ]
