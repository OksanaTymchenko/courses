# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_site', '0005_auto_20170516_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='video',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
