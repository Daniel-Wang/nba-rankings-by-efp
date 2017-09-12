"""
Written by Daniel Wang on September 9th, 2017
This program parses the player data from
texted copied from the Yahoo Fantasy Basketball

Data is formated as:
Player notes
Player name
In game ownership status
GP*
Fan Pts
Pre-Season
Current
% Owned
MPG
FGM
FGA
FTA
FTM
3PTM
PTS
REB
AST
ST
BLK
TO
"""


class Player:

    def __init__(self, name, games_played, points):
        self.name = name
        self.games_played = games_played
        self.points = points

    def print_player(self):
        print (self.name + " " + " | " +
               str(self.games_played) + " | " +
               str(self.points) + " | " + str(self.eff_pts))

    def set_eff_pts(self, pts):
        self.eff_pts = pts
