from django.forms import ModelForm, modelform_factory, ChoiceField
from agents.models import Agent, Player, Account
#from crispy_forms.helper import FormHelper
#from crispy_forms.layout import Submit


class AgentForm(ModelForm):
    class Meta:
        model = Agent
        exclude = ['user']


class PlayerForm(ModelForm):
    class Meta:
        model = Player
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


"""
class AgentForm(forms.Form):
    all_clubs = Club.objects.all()
    club_choices = []
    for club in all_clubs:
        club_choices.append((club.code, club.name))

    nickname = forms.CharField(
        label="Please type nickname of agent",
        max_length=64,
        required=True,
    )

    club_agent_id = forms.IntegerField(
        label="Agent ID",
        required=True,
    )

    club = forms.TypedChoiceField(
        label="which club?",
        choices=club_choices,
        required=True
    )

    rakeback = forms.DecimalField(
        max_digits=3,
        decimal_places=3
    )

    # **as per tutorial
    def __init__(self, *args, **kwargs):
        super(AgentForm, self).__init__(args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-agentForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = "POST"
        self.helper.form_action = "create_agent"

        self.helper.add_input(Submit('submit', 'Submit'))
"""
