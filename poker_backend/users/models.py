from django.db import models
from django.contrib.auth.models import User
from agents.models import Club
# Create your models here.

"""
class UserClubDeal(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="club_deals")
    club = models.ForeignKey(
        Club, on_delete=models.CASCADE, related_name="user_deals")
"""
