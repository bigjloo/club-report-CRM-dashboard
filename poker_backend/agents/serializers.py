from rest_framework import serializers
from .models import Agent, Account, Player

# this serializer inherits from Agent class


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        exclude = ["user"]
        
    def create(self, validated_data):
        return Agent.objects.create(**validated_data)


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ["name"]
