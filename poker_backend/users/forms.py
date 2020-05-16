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

    def __init__(self, *args, **kwargs):
        super(AgentPlayerForm, self).__init__(*args, **kwargs)
        CHOICES = [(1, 'Agent'), (0, 'Player')]
        self.fields['code'].help_text = 'Use Agent ID for agents'
        #self.fields['agent'].choices = CHOICES
        #self.fields['agent'].widget = forms.CheckboxInput


class AccountForm(ModelForm):
    rakeback_percentage = forms.DecimalField(
        min_value=0, decimal_places=3, help_text='Should not be higher than your own')

    chip_value = forms.DecimalField(
        min_value=0.1, decimal_places=2)

    class Meta:
        model = Account
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['agent_players'].queryset = AgentPlayer.objects.filter(
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


class UploadFileForm(forms.Form):

    file = forms.FileField(label="Upload Agent Report",
                           help_text="Upload report")


class UserForm(ModelForm):
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    password2 = forms.CharField(
        max_length=32, widget=forms.PasswordInput, label="Repeat password")

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'password2',
            'email',
        ]
