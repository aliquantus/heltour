# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 02:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0008_team_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=255)),
                ('lichess_username', models.CharField(max_length=255)),
                ('slack_username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('classical_rating', models.PositiveIntegerField()),
                ('peak_classical_rating', models.PositiveIntegerField()),
                ('has_played_20_games', models.BooleanField()),
                ('already_in_slack_group', models.BooleanField()),
                ('previous_season_player', models.CharField(choices=[('new', 'New/returning'), ('alternate', 'Alternate'), ('alternate_to_full_time', 'Alternate to full-time'), ('full_time', 'Full-time')], max_length=255)),
                ('can_commit', models.BooleanField()),
                ('friends', models.CharField(max_length=1023)),
                ('agreed_to_rules', models.BooleanField()),
                ('alternate_preference', models.CharField(choices=[('alternate', 'Alternate'), ('full_time', 'Full Time')], max_length=255)),
                ('weeks_unavailable', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='season',
            name='registration_open',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registration',
            name='season',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Season'),
        ),
    ]
