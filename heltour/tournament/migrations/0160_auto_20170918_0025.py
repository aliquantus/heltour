# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-09-18 00:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import heltour.tournament.models


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0159_auto_20170803_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('lichess_username', models.CharField(blank=True, max_length=255, validators=[django.core.validators.RegexValidator('^[\\w-]+$')])),
                ('slack_user_id', models.CharField(blank=True, max_length=255)),
                ('secret_token', models.CharField(default=heltour.tournament.models.create_api_token, max_length=255, unique=True)),
                ('expires', models.DateTimeField()),
                ('used', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SlackAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('lichess_username', models.CharField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator('^[\\w-]+$')])),
                ('slack_user_id', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='modrequest',
            name='type',
            field=models.CharField(choices=[('withdraw', 'Withdraw'), ('reregister', 'Re-register'), ('appeal_late_response', 'Appeal late response'), ('appeal_noshow', 'Appeal no-show'), ('claim_win_noshow', 'Claim a forfeit win (no-show)'), ('claim_win_effort', 'Claim a forfeit win (insufficient effort)'), ('claim_draw_scheduling', 'Claim a scheduling draw'), ('claim_loss', 'Claim a forfeit loss'), ('request_continuation', 'Request continuation')], max_length=255),
        ),
        migrations.AlterField(
            model_name='playerwarning',
            name='type',
            field=models.CharField(choices=[('unresponsive', 'unresponsive'), ('card_unresponsive', 'card for unresponsive'), ('card_noshow', 'card for no-show')], max_length=255),
        ),
        migrations.AlterField(
            model_name='scheduledevent',
            name='type',
            field=models.CharField(choices=[('notify_mods_unscheduled', 'Notify mods of unscheduled games'), ('notify_mods_no_result', 'Notify mods of games without results'), ('notify_mods_pending_regs', 'Notify mods of pending registrations'), ('start_round_transition', 'Start round transition'), ('notify_players_unscheduled', 'Notify players of unscheduled games'), ('notify_players_game_time', 'Notify players of their game time'), ('automod_unresponsive', 'Auto-mod unresponsive players'), ('automod_noshow', 'Auto-mod no-shows')], max_length=255),
        ),
    ]
