from django.contrib import admin
from leagues.models import *


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    ordering = ('-id',)
    search_fields = ('name', )
    list_per_page = 50


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'nickname', 'bio')
    ordering = ('-id',)
    search_fields = ('name', 'nickname')
    list_per_page = 50


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'league', 'number', 'did_citizen_win')
    ordering = ('-id',)
    search_fields = ('number', 'league')
    list_per_page = 50


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'player', 'player_role', 'win_score', 'extra_score', 'player_position')
    ordering = ('-id',)
    search_fields = ('number', 'comments', 'player_position', 'player')
    list_per_page = 50
