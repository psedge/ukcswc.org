# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-17 05:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='KitForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.CharField(max_length=500)),
                ('area', models.CharField(choices=[('sailing', 'The problem is to do with Sailing / Boat kit \n'), ('windsurfing', 'The problem is to do with  Windsurfing kit \n'), ('clothing', 'The problem is to do with items of clothing \n')], max_length=50)),
            ],
        ),
    ]
