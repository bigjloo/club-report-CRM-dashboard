from django.forms import ModelForm, modelform_factory, ChoiceField
from agents.models import AgentPlayer, Account
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Submit


class AgentForm(ModelForm):
    class Meta:
        model = AgentPlayer
        exclude = ['user']


class PlayerForm(ModelForm):
    class Meta:
        model = AgentPlayer
        exclude = ['user']


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

    def __init__(self, user, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = Agent.objects.filter(user=user)
        self.fields['player'].queryset = Player.objects.filter(user=user)
        #self.fields['agent'].widgets = ChoiceField()
