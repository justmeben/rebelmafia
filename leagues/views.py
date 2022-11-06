from django.shortcuts import render, get_object_or_404
from django.views import View

from leagues.models import League, Game, Player
from leagues.service import get_league_ranking_table


class HomeView(View):
    def get(self, request):
        leagues = League.objects.all()
        context = dict(leagues=leagues)
        return render(request, 'index.html', context=context)


class LeagueView(View):
    def get(self, request, league_id):
        league = get_object_or_404(League, id=league_id)
        players = Player.objects.filter(leagues=league)
        context = dict(league=league, players=players)
        return render(request, 'league.html', context=context)


class LeagueGamesView(View):
    def get(self, request, league_id):
        league = get_object_or_404(League, id=league_id)
        games = Game.objects.prefetch_related('result_set__player').filter(league=league).order_by('number')
        for game in games:
            setattr(game, 'results', game.result_set.all().order_by('player_position'))
        context = dict(league=league, games=games)
        return render(request, 'league_games.html', context=context)


class LeagueTableView(View):
    def get(self, request, league_id):
        league = get_object_or_404(League, id=league_id)
        ranking_table = get_league_ranking_table(league)
        context = dict(league=league, ranking_table=ranking_table)
        return render(request, 'league_table.html', context=context)
