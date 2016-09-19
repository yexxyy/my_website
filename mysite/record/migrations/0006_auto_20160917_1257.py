# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-17 12:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0005_auto_20160915_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecordType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_type', models.CharField(max_length=10, verbose_name='\u7c7b\u578b')),
            ],
            options={
                'verbose_name': '\u7c7b\u578b',
            },
        ),
        migrations.AddField(
            model_name='record',
            name='type',
            field=models.ForeignKey(default=datetime.datetime(2016, 9, 17, 12, 57, 6, 264602, tzinfo=utc), on_delete=django.db.models.deletion.CASCADE, to='record.RecordType', verbose_name='\u7c7b\u578b'),
            preserve_default=False,
        ),
    ]