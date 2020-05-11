from django.forms import ModelForm, modelform_factory, ChoiceField, CharField
from agents.models import AgentPlayer, Account, AccountClub
from django.contrib.auth.models import User
from django import forms
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Submit


class AgentPlayerForm(ModelForm):
    class Meta:
        model = AgentPlayer
        fields = ['nickname', 'code', 'agent']


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['agent_player'].queryset = AgentPlayer.objects.filter(
            user=user)
        #self.fields['player'].queryset = Player.objects.filter(user=user)
        #self.fields['agent'].widgets = ChoiceField()


class AccountClubForm(ModelForm):
    class Meta:
        model = AccountClub
        fields = [
            'rakeback_percentage',
            'chip_value',
        ]
