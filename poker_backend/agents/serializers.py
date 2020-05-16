from rest_framework import serializers
from agents.models import AgentPlayer, Account, Club, AccountClub

# this serializer inherits from Agent class


class AgentPlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = AgentPlayer
        fields = "__all__"


class ClubSerializer(serializers.ModelSerializer):

    agent_players = AgentPlayerSerializer(many=True)

    class Meta:
        model = Club
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    agent_players = AgentPlayerSerializer(many=True)
    clubs = ClubSerializer(many=True)

    class Meta:
        model = Account
        fields = '__all__'


class CreateAccountSerializer(serializers.ModelSerializer):

    agent_players = serializers.IntegerField()
    clubs = serializers.IntegerField()
    rakeback_percentage = serializers.DecimalField(
        max_digits=3, decimal_places=3)
    chip_value = serializers.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = Account
        fields = [
            'nickname',
            'club_account_id',
            'agent_players',
            'clubs',
            'rakeback_percentage',
            'chip_value'
        ]

    def create(self, validated_data):
        print(f"validated_data: {validated_data}")
        rakeback_percentage = validated_data.pop('rakeback_percentage')
        chip_value = validated_data.pop('chip_value')
        club_pk = validated_data.pop('clubs')
        agent_player_pk = validated_data.pop('agent_players')
        try:
            agent_player = AgentPlayer.objects.get(pk=agent_player_pk)
        except AgentPlayer.DoesNotExist:
            return Http404("Agent does not exist")
        try:
            club = Club.objects.get(pk=club_pk)
        except Club.DoesNotExist:
            return Http404('Club does not exist')
        account = Account.objects.create(**validated_data)
        account_club = AccountClub.objects.create(
            account=account, club=club, rakeback_percentage=rakeback_percentage, chip_value=chip_value)
        account.agent_players.add(agent_player)
        account.clubs.add(club)
        account.save()
        account_club.save()
        return account


class AccountClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountClub
        fields = '__all__'
