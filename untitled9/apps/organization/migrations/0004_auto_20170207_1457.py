# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-02-07 14:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20170207_1445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='fav_nums',
            new_name='fav_nims',
        ),
    ]