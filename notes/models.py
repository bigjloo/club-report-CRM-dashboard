from django.db import models
from agents.models import AgentPlayer
# Create your models here.


class Note(models.Model):
    agent_player = models.ForeignKey(
        AgentPlayer, on_delete=models.CASCADE, related_name="notes")
    note = models.TextField()

    def __str__(self):
        return f"{self.agent_player} | {self.note}"
