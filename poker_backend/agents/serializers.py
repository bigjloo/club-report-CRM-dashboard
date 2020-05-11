from rest_framework import serializers
from agents.models import AgentPlayer, Account

# this serializer inherits from Agent class


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentPlayer
        exclude = ["user"]


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentPlayer
        fields = ["name"]


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
