from django.db import models
from django.contrib.auth.models import User
from agents.models import AgentPlayer, Deal

# Create your models here.


class BalanceSheet(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="balance_sheet")
    agent_player = models.OneToOneField(
        AgentPlayer, on_delete=models.CASCADE, null=True, blank=True, related_name="balance_sheet")
    deal = models.OneToOneField(
        Deal, on_delete=models.CASCADE, null=True, blank=True, related_name="balance_sheet")
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    note = models.ForeignKey(
        'notes.Note', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Balance: {self.balance}"


class Transaction(models.Model):
    sender = models.ForeignKey(
        BalanceSheet, on_delete=models.SET_NULL, null=True, related_name="credits")
    reciever = models.ForeignKey(
        BalanceSheet, on_delete=models.SET_NULL, null=True, related_name="debits")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    note = models.ForeignKey(
        'notes.Note', on_delete=models.CASCADE, null=True, blank=True)
