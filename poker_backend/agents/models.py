from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Agent(models.Model):
    nickname = models.CharField(max_length=64)
    club_agent_id = models.IntegerField()
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name="agents")
    rakeback = models.DecimalField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="agents")

    def __str__(self):
        return f"{self.name} - {self.club} - {self.rakeback}"


class Club(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=3)
    platform = [
        ('UP', 'Upoker'),
        ('PB', 'PokerBros'),
        ('PPP', 'PPPoker'),
    ]
    chip_value = models.DecimalField()

    def __str__(self):
        return f"{self.name} ({self.code})"


class Account(models.Model):
    nickname = models.CharField(max_length=64)
    club_account_id = models.IntegerField()
    club = models.ManyToManyField(Club, blank=True, related_name="accounts")

    def __str__(self):
        return f"{self.club_account_id} - {self.nickname}"
