# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-23 18:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complain', '0002_auto_20171221_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='message',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='complain',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
