# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-27 20:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_auto_20170625_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='spouse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=7, unique=True),
        ),
    ]
