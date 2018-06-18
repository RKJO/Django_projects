# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from football.models import *


# Create your views here.


def league_table(request):
    teams = Teams.objects.order_by("-points")
    result = """<html>
        <body> 
            <table>
              <tr>
                <td>No.</td>
                <td>Team</td>
                <td>Points</td>
              </tr> {}
    """
    team_table = ""
    num = 0
    for team in teams:
        num += 1
        team_table += """<tr>
                            <td>{}</td>
                            <td>{}</td>
                            <td>{}</td>
                        </tr>""".format(num, team.name, team.points)
    result += """</table>
                    <body/>
                    <html/>"""

    return HttpResponse(result.format(team_table))


def games_played(request, id):
    teams = Teams.objects.get(id=id)
    result = """<html>
        <body> 
            <table>
              <tr>
                <td><b />Team Home</td>
                <td><b />Team Away</td>
              </tr> {}
    """
    team_table_home = ""
    for game in teams.home.all():
        team_table_home += """<tr>
                            <td>{}</td>
                            <td>{}</td>
                            </tr> 
                            <tr>
                            <td colspan="2"><center /><b />{} : {}</td>
                            </tr>""".format(game.team_home.name,
                                        game.team_away.name,
                                        game.team_home_goals,
                                        game.team_away_goals)
    result += """<tr>
                <td><b />Team Home</td>
                <td><b />Team Away</td>
              </tr> {}"""
    team_table_away = ""
    for game in teams.away.all():
        team_table_away += """<tr>
                            <td>{}</td>
                            <td>{}</td>
                            </tr> 
                            <tr>
                            <td colspan="2"><center /><b />{} : {}</td>
                            </tr>""".format(game.team_home.name,
                                        game.team_away.name,
                                        game.team_home_goals,
                                        game.team_away_goals)
    result += """</table>
                    <body/>
                    <html/>"""

    return HttpResponse(result.format(team_table_home, team_table_away))