# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Teams(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    points = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'


class Games(models.Model):
    id = models.BigAutoField(primary_key=True)
    team_home = models.ForeignKey(Teams, related_name='home', db_column='team_home', on_delete=models.CASCADE, blank=True, null=True)
    team_home_goals = models.BigIntegerField(blank=True, null=True)
    team_away = models.ForeignKey(Teams, related_name='away', db_column='team_away', on_delete=models.CASCADE, blank=True, null=True)
    team_away_goals = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'

