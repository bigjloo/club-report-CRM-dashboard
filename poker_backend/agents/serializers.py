from rest_framework import serializers
from .models import Agent, Account, Player

# this serializer inherits from Agent class


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        exclude = ["user"]


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["name"]


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['nickname', 'club_account_id',
                  'rakeback', 'club', 'agent', 'player']
