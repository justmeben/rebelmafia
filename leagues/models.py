from django.db import models


class League(models.Model):
    name = models.CharField(max_length=128, blank=False, null=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    nickname = models.CharField(max_length=64, blank=False, null=False)
    bio = models.TextField(blank=True, null=True)
    leagues = models.ManyToManyField(League)

    def __str__(self):
        return self.nickname


class Game(models.Model):
    league = models.ForeignKey(League, null=False, blank=False, on_delete=models.DO_NOTHING)
    number = models.IntegerField(null=False, blank=False)
    did_citizen_win = models.BooleanField(null=False, blank=False)

    def __str__(self):
        return f'{self.league.name} - Game #{self.number}'


class Result(models.Model):
    game = models.ForeignKey(Game, null=False, blank=False, on_delete=models.DO_NOTHING)
    player = models.ForeignKey(Player, null=False, blank=False, on_delete=models.DO_NOTHING)
    did_win = models.BooleanField(null=False, blank=False)
    win_score = models.FloatField(null=False, blank=False, default=0)
    extra_score = models.FloatField(null=False, blank=False, default=0)
    plus_score = models.FloatField(null=False, blank=False, default=0)
    minus_score = models.FloatField(null=False, blank=False, default=0)
    player_position = models.IntegerField(null=False, blank=False)
    comments = models.TextField(null=True, blank=True)

    ROLE_CITIZEN = 'Citizen'
    ROLE_SHERIFF = 'Sheriff'
    ROLE_MAFIA = 'Mafia'
    ROLE_DON = 'Don'
    ROLES = (ROLE_CITIZEN, ROLE_SHERIFF, ROLE_MAFIA, ROLE_DON)
    ROLES_CHOICES = (
        (ROLE_CITIZEN, ROLE_CITIZEN),
        (ROLE_SHERIFF, ROLE_SHERIFF),
        (ROLE_MAFIA, ROLE_MAFIA),
        (ROLE_DON, ROLE_DON),
    )

    player_role = models.CharField(choices=ROLES_CHOICES, null=False, blank=False,
                                   default=ROLE_CITIZEN, max_length=16)

    def __str__(self):
        return f'{self.game.__str__()} - Result for {self.player.nickname}'