# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-06 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Point to URL'),
        ),
    ]
