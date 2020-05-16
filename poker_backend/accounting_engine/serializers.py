from .models import Report
from rest_framework import serializers
from agents.serializers import AgentPlayerSerializer, ClubSerializer, AccountSerializer


class ReportSerializer(serializers.ModelSerializer):

    agent_player = AgentPlayerSerializer(required=False)
    account = AccountSerializer(required=False)
    club = ClubSerializer(required=False)

    class Meta:
        model = Report
        exclude = ['created']

    def create(self, validated_data):
        report = Report.objects.create(**validated_data)
        return report

    def to_internal_value(self, data):
        if data.get('insurance') == '':
            data['insurance'] = None
        if data.get('jackpot') == '':
            data['jackpot'] = None
        if data.get('hands') == '':
            data['hands'] = None
        return super(ReportSerializer, self).to_internal_value(data)
