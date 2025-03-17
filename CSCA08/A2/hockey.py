"""Assignment 2: The Hockey Tournament

This code is provided solely for the personal and private use of
students taking the CSCA08 course at the University of Toronto
Scarborough. Copying for purposes other than this use is expressly
prohibited. All forms of distribution of this code, whether as given
or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2024 Bilal Syed

"""

from copy import deepcopy
from typing import TextIO

from constants import (
    F_NAME, L_NAME, AGE, WEIGHT, STATS, TEAM, GP, G, A, TP, G_NUM, T_PLAY, LOC,
    SCORE, HOME, AWAY, H_SCORE, A_SCORE, RESULT, NOTPLAYED, FINAL, ROUND)


# We provide this sample data to help you set up example calls.
FIVE_PLAYERS = [
    ['Filip', 'Forsberg', 18, 189.7, [5, 0, 3, 3], 'Warriors'],
    ['Ryan', 'Rielly', 27, 207.9, [3, 3, 1, 4], 'Pirates'],
    ['Roman', 'Josi', 35, 170.0, [4, 0, 7, 7], 'Pirates'],
    ['Ryan', 'Thomas', 28, 205.2, [3, 1, 3, 4], 'Warriors'],
    ['Jason', 'Zucker', 21, 220.3, [5, 3, 3, 6], 'Pirates']
]

FIVE_GAMES = [
    [1, ['Warriors', 'Pirates'], 'Toronto', [2, 3, 'FINAL']],
    [2, ['Leafs', 'Bruins'], 'Toronto', [0, 0, 'NOTPLAYED']],
    [3, ['Pirates', 'Youngstars'], 'Mississauga', [5, 7, 'FINAL']],
    [4, ['Leafs', 'Warriors'], 'Oshawa', [0, 0, 'NOTPLAYED']],
    [5, ['Bruins', 'Youngstars'], 'Mississauga', [0, 7, 'FINAL']]
]


# We provide the header and docstring for this function to help you get
# started.
def get_player(players: list[list], f_name: str, l_name: str) -> list:
    '''Return the player with the given first name 'f_name' and last
    name 'l_name' in the list of players 'players'. Return an empty list if
    no such player exists.
    
    Pre-condition: 'players' is a valid list of players.
    
    >>> get_player(FIVE_PLAYERS, 'Roman', 'Josi')
    ['Roman', 'Josi', 35, 170.0, [4, 0, 7, 7], 'Pirates']
    >>> player = ['Ryan', 'Rielly', 27, 207.9, [3, 3, 1, 4], 'Pirates']
    >>> get_player(FIVE_PLAYERS, 'Ryan', 'Rielly') == player
    True
    >>> get_player(FIVE_PLAYERS, 'Bilal', 'Syed')
    []
    '''
    for player in players:
        if player[F_NAME] == f_name and player[L_NAME] == l_name:
            return player
    return []


# We provide the header and doctring for this function to help get you
# started.
def get_game(games: list[list], game_num: int) -> list:
    '''Return the game with the given game number 'game_num' in the list of
    games 'games'. Return an empty list if no such game exists.
    
    Pre-condition: 'games' is a valid list of games.
    
    >>> result = get_game(FIVE_GAMES, 2)
    >>> result == [2, ['Leafs', 'Bruins'], 'Toronto', [0, 0, 'NOTPLAYED']]
    True
    >>> get_game(FIVE_GAMES, 5)
    [5, ['Bruins', 'Youngstars'], 'Mississauga', [0, 7, 'FINAL']]
    >>> get_game(FIVE_GAMES, 7)
    []
    '''
    for game in games:
        if game[G_NUM] == game_num:
            return game
    return []


# We provide the header and doctring for this function to help get you
# started. Note the use of the built-in function deepcopy (see
# help(deepcopy)!): since this function modifies its input, we do not
# want to call it with FIVE_PLAYERS, which would interfere with the
# use of FIVE_PLAYERS in examples for other functions.
def update_player_stats(players: list[list], f_name: str, l_name: str,
                        goals: int, assists: int) -> None:
    '''Update the player in the list of players 'players' with given
    first name 'f_name' and last name 'l_name' such that the given goals
    'goals' and assists 'assists' are added to their stats. This player's games
    played will increase by 1 and their total points will also be updated
    accordingly. If such a player doesn't exist, 'players' will remain
    unchanged.
    
    Pre-condition: 'players' is a valid list of players. 'goals' >= 0.
    'assists' >= 0.
    
    >>> five_players = deepcopy(FIVE_PLAYERS)
    >>> update_player_stats(five_players, 'Filip', 'Forsberg', 1, 1)
    >>> five_players == [
    ...   ['Filip', 'Forsberg', 18, 189.7, [6, 1, 4, 5], 'Warriors'],
    ...   ['Ryan', 'Rielly', 27, 207.9, [3, 3, 1, 4], 'Pirates'],
    ...   ['Roman', 'Josi', 35, 170.0, [4, 0, 7, 7], 'Pirates'],
    ...   ['Ryan', 'Thomas', 28, 205.2, [3, 1, 3, 4], 'Warriors'],
    ...   ['Jason', 'Zucker', 21, 220.3, [5, 3, 3, 6], 'Pirates']]
    True
    >>> five_players = deepcopy(FIVE_PLAYERS)
    >>> update_player_stats(five_players, 'Bilal', 'Syed', 2, 3)
    >>> five_players == [
    ...   ['Filip', 'Forsberg', 18, 189.7, [5, 0, 3, 3], 'Warriors'],
    ...   ['Ryan', 'Rielly', 27, 207.9, [3, 3, 1, 4], 'Pirates'],
    ...   ['Roman', 'Josi', 35, 170.0, [4, 0, 7, 7], 'Pirates'],
    ...   ['Ryan', 'Thomas', 28, 205.2, [3, 1, 3, 4], 'Warriors'],
    ...   ['Jason', 'Zucker', 21, 220.3, [5, 3, 3, 6], 'Pirates']]
    True
    '''
    player = get_player(players, f_name, l_name)
    if len(player) > 0:
        player[STATS][GP] += 1
        player[STATS][G] += goals
        player[STATS][A] += assists
        player[STATS][TP] += goals + assists
        

# This is a suggested helper function for check_player_attendance. We provide
# the header and doctring to help you structure your solution.
def get_num_of_played_games(games: list[list], team: str) -> int:
    '''Return the number of games played by team 'team' as per given list of
    games 'games'.
    
    Pre-condition: 'games' is a valid list of games.
    
    >>> get_num_of_played_games(FIVE_GAMES, 'Pirates')
    2
    >>> get_num_of_played_games(FIVE_GAMES, 'Warriors')
    1
    >>> get_num_of_played_games(FIVE_GAMES, 'Leafs')
    0
    >>> get_num_of_played_games(FIVE_GAMES, 'Sens')
    0
    '''
    games_played = 0
    for game in games:
        if game[SCORE][RESULT] == FINAL and team in game[T_PLAY]:
            games_played += 1
    return games_played


def update_game_score(games: list[list], game_num: int, home_score: int,
                      away_score: int) -> None:
    '''Update the home team score and away team score of a game in given list of
    games 'games' with given game number 'game_num'. If the game does not exist
    or has already been played, the game remains unchanged.
    
    Pre-condition: 'games' is a valid list of games. At least one of the team's
    scores is greater than the other.
    
    >>> five_games = deepcopy(FIVE_GAMES)
    >>> update_game_score(five_games, 2, 1, 2)
    >>> five_games == [
    ... [1, ['Warriors', 'Pirates'], 'Toronto', [2, 3, 'FINAL']],
    ... [2, ['Leafs', 'Bruins'], 'Toronto', [1, 2, 'FINAL']],
    ... [3, ['Pirates', 'Youngstars'], 'Mississauga', [5, 7, 'FINAL']],
    ... [4, ['Leafs', 'Warriors'], 'Oshawa', [0, 0, 'NOTPLAYED']],
    ... [5, ['Bruins', 'Youngstars'], 'Mississauga', [0, 7, 'FINAL']]
    ... ]
    True
    >>> five_games = deepcopy(FIVE_GAMES)
    >>> update_game_score(five_games, 1, 1, 2)
    >>> five_games == [
    ... [1, ['Warriors', 'Pirates'], 'Toronto', [2, 3, 'FINAL']],
    ... [2, ['Leafs', 'Bruins'], 'Toronto', [0, 0, 'NOTPLAYED']],
    ... [3, ['Pirates', 'Youngstars'], 'Mississauga', [5, 7, 'FINAL']],
    ... [4, ['Leafs', 'Warriors'], 'Oshawa', [0, 0, 'NOTPLAYED']],
    ... [5, ['Bruins', 'Youngstars'], 'Mississauga', [0, 7, 'FINAL']]
    ... ]
    True
    '''
    game = get_game(games, game_num)
    if len(game) > 0 and game[SCORE][RESULT] == NOTPLAYED:
        game[SCORE][H_SCORE] = home_score
        game[SCORE][A_SCORE] = away_score
        game[SCORE][RESULT] = FINAL
        
        
def get_total_score(games: list[list], team: str) -> int:
    '''Return total number of goals scored by given team 'team' according to
    given list of games 'games'. If team does not exist, return 0.
    
    Pre-condition: 'games' is a valid list of games.
    
    >>> get_total_score(FIVE_GAMES, 'Pirates')
    8
    >>> five_games = deepcopy(FIVE_GAMES)
    >>> update_game_score(five_games, 2, 1, 2)
    >>> get_total_score(five_games, 'Leafs')
    1
    '''
    total_score = 0
    for game in games:
        if team in game[T_PLAY]:
            if game[T_PLAY][HOME] == team:
                goals_scored += game[SCORE][H_SCORE]
            else:
                goals_scored += game[SCORE][A_SCORE]
    return goals_scored
            
            
def get_ppg(players: list[list], f_name: str, l_name: str) -> float:
    '''Return the points per game rounded by constant ROUND of a player with
    given first name 'f_name' and last name 'l_name' from given list of players
    'players'. If player does not exist, return 0.
    
    Pre-condition: 'players' is a valid list of players.
    
    >>> get_ppg(FIVE_PLAYERS, 'Filip', 'Forsberg')
    0.6
    >>> get_ppg(FIVE_PLAYERS, 'Ryan', 'Rielly')
    1.33
    '''
    player = get_player(players, f_name, l_name)
    if len(player) > 0 and player[STATS][GP] != 0:
        return round(player[STATS][TP] / player[STATS][GP], ROUND)
    return 0
    
    
def add_player(players: list[list], f_name: str, l_name: str,
               new_player: list) -> None:
    '''Update the given list of players 'players' by adding new player
    'new_player' just before player with given first name 'f_name' and last name
    'l_name'. If player with given first name and last name does not exist, add
    new player to end of list.
    
    Pre-condition: 'players' is a valid list of players. 'new_player' is a valid
    player. 'new_player's' first and last name are unique - a player with their
    first and last name do not exist in the given list of players.
    
    >>> five_players = deepcopy(FIVE_PLAYERS)
    >>> add_player(five_players, 'Filip', 'Forsberg', ['Daniel', 'Duris', 29,
    ... 182.5, [1, 2, 3, 5], 'Warriors'])
    >>> five_players == [
    ...   ['Daniel', 'Duris', 29, 182.5, [1, 2, 3, 5], 'Warriors'],
    ...   ['Filip', 'Forsberg', 18, 189.7, [5, 0, 3, 3], 'Warriors'],
    ...   ['Ryan', 'Rielly', 27, 207.9, [3, 3, 1, 4], 'Pirates'],
    ...   ['Roman', 'Josi', 35, 170.0, [4, 0, 7, 7], 'Pirates'],
    ...   ['Ryan', 'Thomas', 28, 205.2, [3, 1, 3, 4], 'Warriors'],
    ...   ['Jason', 'Zucker', 21, 220.3, [5, 3, 3, 6], 'Pirates']]
    True
    >>> five_players = deepcopy(FIVE_PLAYERS)
    >>> add_player(five_players, 'Ty', 'Arbour', ['Cliff', 'Barton', 25, 193.2,
    ... [5, 4, 3, 7], 'Pirates'])
    >>> five_players == [
    ...   ['Filip', 'Forsberg', 18, 189.7, [5, 0, 3, 3], 'Warriors'],
    ...   ['Ryan', 'Rielly', 27, 207.9, [3, 3, 1, 4], 'Pirates'],
    ...   ['Roman', 'Josi', 35, 170.0, [4, 0, 7, 7], 'Pirates'],
    ...   ['Ryan', 'Thomas', 28, 205.2, [3, 1, 3, 4], 'Warriors'],
    ...   ['Jason', 'Zucker', 21, 220.3, [5, 3, 3, 6], 'Pirates'],
    ...   ['Cliff', 'Barton', 25, 193.2, [5, 4, 3, 7], 'Pirates']]
    True
    '''
    player = get_player(players, f_name, l_name)
    if len(player) > 0:
        player_index = players.index(player)
        players.insert(player_index, new_player)
    else:
        players.append(new_player)
        
        
def get_best_game(games: list[list]) -> list:
    '''Return the game from given list of games 'games' with most goals scored.
    If multiple games are tied, return the first one, and if list of games is
    empty, return an empty list.
    
    Pre-condition: 'games' is a valid list of games.
    
    >>> get_best_game(FIVE_GAMES)
    [3, ['Pirates', 'Youngstars'], 'Mississauga', [5, 7, 'FINAL']]
    >>> five_games = deepcopy(FIVE_GAMES)
    >>> update_game_score(five_games, 4, 6, 7)
    >>> get_best_game(five_games)
    [4, ['Leafs', 'Warriors'], 'Oshawa', [6, 7, 'FINAL']]
    '''
    if len(games) > 0:
        best_game = games[0]
        for game in games:
            game_goals = game[SCORE][H_SCORE] + game[SCORE][A_SCORE]
            best_game_goals = (best_game[SCORE][H_SCORE]
                               + best_game[SCORE][A_SCORE])
            if best_game_goals < game_goals:
                best_game = game
        return best_game
    return []


def get_best_player(players: list[list]) -> list:
    '''Return the player from the given list of players 'players' with the
    highest points per game. If multiple players are tied, return the last one
    and if the list of players is empty, return an empty list.
    
    Pre-condition: 'players' is a valid list of players.
    
    >>> get_best_player(FIVE_PLAYERS)
    ['Roman', 'Josi', 35, 170.0, [4, 0, 7, 7], 'Pirates']
    >>> five_players = deepcopy(FIVE_PLAYERS)
    >>> add_player(five_players, 'Filip', 'Forsberg', ['Daniel', 'Duris', 29,
    ... 182.5, [1, 2, 3, 5], 'Warriors'])
    >>> get_best_player(five_players)
    ['Daniel', 'Duris', 29, 182.5, [1, 2, 3, 5], 'Warriors']
    '''
    if len(players) > 0:
        best_player = players[0]
        for player in players:
            player_ppg = get_ppg(players, player[F_NAME], player[L_NAME])
            best_player_ppg = get_ppg(players, best_player[F_NAME],
                                      best_player[L_NAME])
            if best_player_ppg <= player_ppg:
                best_player = player
        return best_player
    return []


def get_notplayed_games(games: list[list]) -> list[int]:
    '''Return the game number of unplayed games from list of games 'games'. If
    there are no unplayed games, return an empty list.
    
    Pre-condition: 'games' is a valid list of games.
    
    >>> get_notplayed_games(FIVE_GAMES)
    [2, 4]
    >>> five_games = deepcopy(FIVE_GAMES)
    >>> update_game_score(five_games, 4, 6, 7)
    >>> get_notplayed_games(five_games)
    [2]
    '''
    unplayed_games = []
    for game in games:
        if game[SCORE][RESULT] == NOTPLAYED:
            unplayed_games.append(game[G_NUM])
    return unplayed_games


def check_player_attendance(games: list[list], players: list[list]) -> bool:
    '''Return True if and only if every player in given list of players
    'players' have played in all their team's games as per the given list of
    games 'games'.
    
    Pre-condition: 'games' is a valid list of games. 'players' is a valid list
    of players. Players only play in their own team's games.
    
    >>> check_player_attendance(FIVE_GAMES, FIVE_PLAYERS)
    True
    >>> five_games = [
    ... [1, ['Warriors', 'Pirates'], 'Toronto', [2, 3, 'FINAL']],
    ... [2, ['Pirates', 'Bruins'], 'Toronto', [3, 2, 'FINAL']],
    ... [3, ['Pirates', 'Youngstars'], 'Mississauga', [5, 7, 'FINAL']],
    ... [4, ['Leafs', 'Pirates'], 'Oshawa', [6, 4, 'FINAL']],
    ... [5, ['Bruins', 'Youngstars'], 'Mississauga', [0, 7, 'FINAL']]
    ... ]
    >>> check_player_attendance(five_games, FIVE_PLAYERS)
    False
    '''
    for player in players:
        if player[STATS][GP] < get_num_of_played_games(games, player[TEAM]):
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
