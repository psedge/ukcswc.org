# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-21 05:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasters', '0003_auto_20160819_1916'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='usersession',
            unique_together=set([('user', 'date', 'time')]),
        ),
    ]
