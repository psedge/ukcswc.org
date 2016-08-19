# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-19 14:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Spot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasters.Date')),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasters.Time')),
            ],
        ),
        migrations.AlterModelOptions(
            name='usersession',
            options={'verbose_name': 'Taster Session', 'verbose_name_plural': 'Taster Sessions'},
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
    ]