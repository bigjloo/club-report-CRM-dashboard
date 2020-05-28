from rest_framework import serializers
from .models import BalanceSheet, Transaction


class BalanceSheetSerializer(serializers.Serializer):
    class Meta:
        model = BalanceSheet
        fields = ['balance']


class TransactionSerializer(serializers.Serializer):
    class Meta:
        model = Transaction
        exlude = ['note']
