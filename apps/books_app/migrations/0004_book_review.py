# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-21 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0003_remove_book_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='review',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='books_app.Review'),
            preserve_default=False,
        ),
    ]
