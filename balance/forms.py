from django.forms import ModelForm
from .models import Transaction
from itertools import chain
from agents.models import AgentPlayer, Deal
from django import forms


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        exclude = ['notes']

    def __init__(self, user, *args, **kwargs):
        super(TransactionForm, self).__init__(*args, **kwargs)
        agent_players = user.agent_players.all()
        deals = user.club_deals.all()
        self.fields['sender'].queryset = chain(agent_players, deals)
