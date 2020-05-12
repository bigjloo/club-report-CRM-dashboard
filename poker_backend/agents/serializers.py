from rest_framework import serializers
from agents.models import AgentPlayer, Account

# this serializer inherits from Agent class


class AgentPlayerSerializer(serializers.ModelSerializer):
    #user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = AgentPlayer
        #fields = "__all__"
        exclude = ['user']


class AccountSerializer(serializers.ModelSerializer):

    """
    agent_players = serializers.PrimaryKeyRelatedField(
        many=True, queryset=AgentPlayer.objects.all())
    """

    class Meta:
        model = Account
        fields = [
            'nickname',
            'club_account_id',
            'agent_player',
            'clubs',
        ]
