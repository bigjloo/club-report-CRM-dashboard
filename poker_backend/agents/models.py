from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal
# Create your models here.


class AgentPlayer(models.Model):

    options = (
        (1, 'Agent'),
        (0, 'Player'),
    )
    nickname = models.CharField(max_length=64)
    code = models.CharField(max_length=12, unique=True)
    #rakeback = models.DecimalField(max_digits=3, decimal_places=3)
    agent = models.IntegerField(choices=options, default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='agent_players')

    def __str__(self):
        return f"{self.nickname} ({self.code})"


class Club(models.Model):
    PLATFORMS = (
        ('UP', 'Upoker'),
        ('PB', 'PokerBros'),
        ('PPP', 'PPPoker'),
        ('ANP', 'All New Poker'),
        ('PT', 'PokerTime'),
    )
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=3)
    club_id = models.IntegerField(unique=True)
    chip_value = models.DecimalField(max_digits=3, decimal_places=2, validators=[
                                     MinValueValidator(Decimal('0.01'))])
    platform = models.CharField(max_length=3, choices=PLATFORMS, default='PB')
    agent_players = models.ManyToManyField(
        AgentPlayer, through='Deal', related_name='clubs')

    def __str__(self):
        return f"{self.name} ({self.code}) - {self.club_id}"


class Deal(models.Model):
    agent_player = models.ForeignKey(
        AgentPlayer, on_delete=models.SET_NULL, null=True, related_name='deals')
    club = models.ForeignKey(
        Club, on_delete=models.SET_NULL, null=True, related_name='agent_deals')
    rakeback_percentage = models.DecimalField(
        max_digits=3, decimal_places=3, validators=[MinValueValidator(Decimal('0.01'))])
    chip_value = models.DecimalField(max_digits=3, decimal_places=2, validators=[
                                     MinValueValidator(Decimal('0.01'))])

    class Meta:
        unique_together = ('agent_player', 'club')

    def __str__(self):
        return f"{self.agent_player.nickname} ({self.agent_player.code}) is in {self.club.name} with RB = ({self.rakeback_percentage}), 1 chip = {self.chip_value}"


class Account(models.Model):
    nickname = models.CharField(max_length=64)
    club_account_id = models.IntegerField()
    agent_players = models.ManyToManyField(
        AgentPlayer, related_name="accounts", blank=True)
    clubs = models.ManyToManyField(
        Club, through='AccountClub', related_name='accounts', blank=True)

    def __str__(self):
        return f"{self.nickname} ({self.club_account_id})"


class AccountClub(models.Model):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name='club_deal')
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name='account_deal')
    rakeback_percentage = models.DecimalField(
        max_digits=3, decimal_places=3, validators=[MinValueValidator(Decimal('0.0'))])
    chip_value = models.DecimalField(max_digits=5, decimal_places=2, validators=[
                                     MinValueValidator(Decimal('0.01'))])

    def __str__(self):
        return f"{self.account.nickname} belongs to {self.club.name} with rakeback of {self.rakeback_percentage} and chip value of {self.chip_value}"
