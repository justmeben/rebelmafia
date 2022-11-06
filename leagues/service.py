from typing import List
from leagues.models import League, Player, Game, Result


def get_league_ranking_table(league: League) -> List:
    results = Result.objects.select_related('player').filter(game__league=league)
    players_data = {}
    for result in results:
        if result.player_id not in players_data.keys():
            players_data[result.player_id] = dict(id=result.player_id, nickname=result.player.nickname,
                                                  position=0, total_points=0, total_extra_points=0,
                                                  total_plus_points=0, total_minus_points=0, wins=0, losses=0,
                                                  total_games=0, winrate=0)
        players_data[result.player_id]['total_points'] += result.win_score + result.extra_score
        players_data[result.player_id]['total_extra_points'] += result.extra_score
        players_data[result.player_id]['total_plus_points'] += result.plus_score
        players_data[result.player_id]['total_minus_points'] += result.minus_score
        if result.did_win:
            players_data[result.player_id]['wins'] += 1
        else:
            players_data[result.player_id]['losses'] += 1
        players_data[result.player_id]['total_games'] += 1
        players_data[result.player_id]['winrate'] = 100 * players_data[result.player_id]['wins'] / players_data[result.player_id]['total_games']

    ranking_table = sorted(players_data.values(), key=lambda x: x.get('total_points', -1), reverse=True)
    for i in range(len(ranking_table)):
        ranking_table[i]['position'] = i+1

    return ranking_table
