# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 18:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flashcard', '0007_flashcard_page_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcard',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flashcard',
            name='published_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
