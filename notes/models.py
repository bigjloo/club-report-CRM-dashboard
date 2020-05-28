from django.db import models
from agents.models import AgentPlayer
from balance.models import Transaction, BalanceSheet
# Create your models here.


class Note(models.Model):
    note = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.created} | {self.note}"


class Announcement(models.Model):
    announcement = models.TextField()
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.created}: {self.announcement}"
