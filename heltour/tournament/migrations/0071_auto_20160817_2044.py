# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-17 20:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0070_auto_20160816_0552'),
    ]

    operations = [
        migrations.CreateModel(
            name='LateRegisterRoundChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('retroactive_byes', models.PositiveIntegerField(default=0)),
                ('late_join_points', models.PositiveIntegerField(default=0)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Player')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Round')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerBye',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(choices=[('full-point-bye', 'Full-Point Bye'), ('half-point-bye', 'Half-Point Bye'), ('zero-point-bye', 'Zero-Point Bye')], max_length=31)),
                ('player_rank', models.PositiveIntegerField(blank=True, null=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Player')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Round')),
            ],
        ),
        migrations.CreateModel(
            name='WithdrawRoundChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Player')),
                ('round', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Round')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='WithdrawRoundChange',
            unique_together=set([('round', 'player')]),
        ),
        migrations.AlterUniqueTogether(
            name='playerbye',
            unique_together=set([('round', 'player')]),
        ),
        migrations.AlterUniqueTogether(
            name='LateRegisterRoundChange',
            unique_together=set([('round', 'player')]),
        ),
        migrations.RunSQL('''
        INSERT INTO tournament_LateRegisterRoundChange ( round_id, player_id, date_created, date_modified, retroactive_byes, late_join_points )
                             SELECT DISTINCT round_id, player_id, NOW(), NOW(), 0, 0 FROM tournament_roundchange WHERE action='register';
        INSERT INTO tournament_WithdrawRoundChange ( round_id, player_id, date_created, date_modified )
                             SELECT DISTINCT round_id, player_id, NOW(), NOW() FROM tournament_roundchange WHERE action='withdraw';
        INSERT INTO tournament_playerbye ( round_id, player_id, type, date_created, date_modified )
                             SELECT DISTINCT round_id, player_id, action, NOW(), NOW() FROM tournament_roundchange WHERE action='half-point-bye';
        ''')
    ]