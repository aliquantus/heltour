# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-13 23:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0058_auto_20160813_2314'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LonePlayerPairing',
            new_name='LonePlayerPairing_old',
        ),
        migrations.RenameModel(
            old_name='TeamPlayerPairing',
            new_name='TeamPlayerPairing_old',
        ),
    ]
