# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 11:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_site', '0004_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
