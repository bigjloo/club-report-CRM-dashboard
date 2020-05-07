from django.db import models
from agents.models import Agent, Account

# Create your models here.


class Report(models.Model):
    gross_winloss = models.DecimalField(max_digits=7, decimal_places=2)
    total_rake = models.DecimalField(max_digits=7, decimal_places=2)
    rakeback_earnings = models.DecimalField(max_digits=7, decimal_places=2)
    net_winloss = models.DecimalField(max_digits=7, decimal_places=2)
    created = models.DateField(auto_now_add=True)
    agent = models.ForeignKey(
        Agent, on_delete=models.CASCADE, related_name="reports")
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="reports")

    def __str__(self):
        return f"W/L: {self.gross_winloss} | RAKE: {self.total_rake} | RB: {self.rakeback_earnings} | NET: {self.net_winloss}"
