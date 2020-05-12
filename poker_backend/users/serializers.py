from django.contrib.auth.models import User
from rest_framework import serializers
from agents.models import AgentPlayer


class UserSerializer(serializers.ModelSerializer):
    agent_players = serializers.PrimaryKeyRelatedField(
        many=True, queryset=AgentPlayer.objects.all())

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'agent_players',
        ]
