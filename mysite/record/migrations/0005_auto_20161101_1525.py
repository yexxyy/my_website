# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-01 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0004_auto_20161101_1152'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u59d3\u540d')),
                ('mail', models.CharField(max_length=100, verbose_name='\u90ae\u7bb1')),
                ('phone', models.CharField(max_length=100, verbose_name='\u7535\u8bdd')),
                ('message', models.TextField(verbose_name='\u5907\u6ce8\u4fe1\u606f')),
            ],
            options={
                'verbose_name': '\u5ba2\u6237',
                'verbose_name_plural': '\u5ba2\u6237\u8054\u7cfb\u6570\u636e',
            },
        ),
        migrations.AlterModelOptions(
            name='record',
            options={'verbose_name': '\u8bb0\u5f55', 'verbose_name_plural': '\u65f6\u95f4\u8f74'},
        ),
    ]