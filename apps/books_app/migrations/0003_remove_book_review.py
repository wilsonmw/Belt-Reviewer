# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-21 22:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0002_auto_20170721_2246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='review',
        ),
    ]
