from rest_framework import serializers
from notes.models import Note
from agents.serializers import AgentPlayerSerializer


class NoteSerializer(serializers.ModelSerializer):
    agent_player = AgentPlayerSerializer()

    class Meta:
        model = Note
        fields = '__all__'
