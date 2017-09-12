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

from Player import Player

FILE_NAMES = ["data-15-16.txt", "data-16-17.txt"]
total_player_list = {}

for name in FILE_NAMES:

    file = open(name, 'r')

    player_list = []
    TOTAL_GAMES = 82

    is_end_of_file = file.readline()
    while is_end_of_file:
        name = file.readline().rstrip('\n')
        file.readline()
        gp = float(file.readline().rstrip('\n'))
        points = float(file.readline().rstrip('\n'))
        for count in range(1, 17):
            file.readline()

        player = Player(name, gp, points)
        if gp > 19:
            player_list.append(player)
        # player.print_player()

        is_end_of_file = file.readline()

    # Sort the players by gp/80 * fantasy points
    for player in player_list:
        player.set_eff_pts(player.games_played / TOTAL_GAMES *
                           player.points)
        player_exists = total_player_list.get(player.name, "")
        if (player_exists != ""):
            player_exists.games_played = str((player_exists.games_played +
                                              player.games_played) / 2)
            player_exists.points = str((player_exists.points +
                                        player.points) / 2)
            player_exists.eff_pts = (player_exists.eff_pts +
                                     player.eff_pts) / 2
            total_player_list[player.name] = player_exists
        else:
            total_player_list[player.name] = player

    file.close()

player_ranking = total_player_list.values()
player_ranking.sort(key=lambda x: float(x.eff_pts), reverse=True)

for player in player_ranking:
    player.print_player()
