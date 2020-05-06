from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Club(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=3)
    platforms = (
        ('UP', 'Upoker'),
        ('PB', 'PokerBros'),
        ('PPP', 'PPPoker'),
    )
    chip_value = models.DecimalField(max_digits=3, decimal_places=2)
    platform = models.CharField(max_length=3, choices=platforms, default='PB')

    def __str__(self):
        return f"{self.name} ({self.code})"


class Agent(models.Model):
    nickname = models.CharField(max_length=64)
    club_agent_id = models.IntegerField()
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name="agents")
    rakeback = models.DecimalField(max_digits=3, decimal_places=3)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="agents")

    def __str__(self):
        return f"{self.nickname} - {self.club} - {self.rakeback}"


class Account(models.Model):
    nickname = models.CharField(max_length=64)
    club_account_id = models.IntegerField()
    club = models.ManyToManyField(Club, blank=True, related_name="accounts")
    agent = models.ManyToManyField(Agent, related_name="accounts")

    def __str__(self):
        return f"{self.club_account_id} - {self.nickname}"
