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
    code = models.CharField(max_length=12)
    #rakeback = models.DecimalField(max_digits=3, decimal_places=3)
    agent = models.IntegerField(choices=options, default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='agent_players')
    note = models.ForeignKey(
        'notes.Note', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        unique_together = ('code', 'user')

    def __str__(self):
        return f"{self.nickname} ({self.code})"


class Club(models.Model):
    PLATFORMS = [
        ('UP', 'Upoker'),
        ('PB', 'PokerBros'),
        ('PPP', 'PPPoker'),
        ('ANP', 'All New Poker'),
        ('PT', 'PokerTime'),
        ('PM', 'PokerMaster'),
    ]
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=3)
    club_id = models.IntegerField(unique=True)
    platform = models.CharField(max_length=3, choices=PLATFORMS, default='PB')
    users = models.ManyToManyField(
        User, through='Deal', related_name='clubs')

    class Meta:
        unique_together = ('code', 'platform')

    def __str__(self):
        return f"{self.name} ({self.code}) - {self.club_id}"


class Deal(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='club_deals')
    club = models.ForeignKey(
        Club, on_delete=models.SET_NULL, null=True, related_name='agent_deals')
    rakeback_percentage = models.DecimalField(
        max_digits=3, decimal_places=3, validators=[MinValueValidator(Decimal('0.01'))])
    chip_value = models.DecimalField(max_digits=3, decimal_places=2, validators=[
                                     MinValueValidator(Decimal('0.01'))])
    referral_id = models.IntegerField(blank=True, null=True)

    class Meta:
        unique_together = (['user', 'club', 'referral_id'])

    def __str__(self):
        return f"{self.club.name} | RB = ({self.rakeback_percentage}) | 1  = {self.chip_value}"


class Account(models.Model):
    nickname = models.CharField(max_length=64)
    club_account_id = models.IntegerField()
    agent_players = models.ManyToManyField(
        AgentPlayer, related_name="accounts", blank=True)
    clubs = models.ManyToManyField(
        Club, through='AccountClub', related_name='accounts', blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='accounts')

    class Meta:
        unique_together = (['user', 'club_account_id'])

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
        return f"{self.account.nickname} | {self.club.name} | {round(self.rakeback_percentage * 100, 1)}% | {self.chip_value}"
