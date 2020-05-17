from django.db import models
from agents.models import AgentPlayer, Club, Account

# Create your models here.


class Report(models.Model):
    gross_winloss = models.DecimalField(max_digits=7, decimal_places=2)
    total_rake = models.DecimalField(max_digits=7, decimal_places=2)
    insurance = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    jackpot = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    rakeback = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    net_winloss = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    net_winloss_fiat = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    hands = models.IntegerField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    agent_player = models.ForeignKey(
        AgentPlayer, on_delete=models.SET_NULL, null=True, related_name="reports", blank=True)
    account = models.ForeignKey(
        Account, on_delete=models.SET_NULL, null=True, related_name="reports", blank=True)
    club = models.ForeignKey(
        Club, on_delete=models.SET_NULL,  null=True, related_name="reports", blank=True)

    def __str__(self):
        return f"{self.account}: W/L: {self.gross_winloss} | RAKE: {self.total_rake} "


# class AgentReport(models.Model):
#    gross_winloss = models.DecimalField(max_digits=7, decimal_places=2)
#    total_rake = models.DecimalField(max_digits=7, decimal_places=2)
#    rakeback_earnings = models.DecimalField(max_digits=7, decimal_places=2)
#    net_winloss = models.DecimalField(max_digits=7, decimal_places=2)
#    insurance = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
#    jackpot = models.DecimalField(max_digits=7, decimal_places=2, blank=True)
#    hands = models.IntegerField(blank=True)
#    created = models.DateField(auto_now_add=True)
#    agent = models.ForeignKey(
#        AgentPlayer, on_delete=models.CASCADE, related_name="reports")

#    def __str__(self):
#        return f"W/L: {self.gross_winloss} | RAKE: {self.total_rake} | RB: {self.rakeback_earnings} | NET: {self.net_winloss}"
