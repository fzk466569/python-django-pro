# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-10 21:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170210_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='\u751f\u65e5'),
        ),
    ]
