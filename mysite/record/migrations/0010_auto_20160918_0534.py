# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-18 05:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0009_auto_20160918_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='record_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.RecordType', verbose_name='\u7c7b\u578b'),
        ),
    ]