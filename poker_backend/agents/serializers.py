from rest_framework import serializers
from agents.models import AgentPlayer, Account

# this serializer inherits from Agent class


class AgentPlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentPlayer
        exclude = ["user"]


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'nickname',
            'club_account_id',
            'rakeback',
            'club',
            'agent',
            'player',
        ]
