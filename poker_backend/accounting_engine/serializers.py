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


class CleanReportSerializer(serializers.ModelSerializer):
    account = AccountSerializer(read_only=True)
    club = ClubSerializer(read_only=True)
    rakeback = serializers.DecimalField(
        max_digits=3, decimal_places=3, required=False)
    net_winloss = serializers.DecimalField(
        max_digits=3, decimal_places=3, required=False)
    #chip_value = serializers.DecimalField(max_digits=3, decimal_places=3)

    class Meta:
        model = Report
        fields = [
            'account',
            'club',
            'gross_winloss',
            'total_rake',
            'rakeback',
            'net_winloss',

        ]

    def to_internal_value(self, data):
        rakeback_percentage = self.account.club_deal.get(
            club=self.club).rakeback_percentage
        data['rakeback'] = self.total_rake * rakeback_percentage
        return super(CleanReportSerializer, self).to_internal_value(data)
