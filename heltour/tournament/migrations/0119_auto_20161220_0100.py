# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-20 01:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0118_auto_20161220_0055'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LeagueNotification',
            new_name='LeagueChannel',
        ),
    ]