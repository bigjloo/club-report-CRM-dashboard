from django.shortcuts import render
from .models import AccountReport, AgentReport, Account, Agent
from django.contrib.auth.models import User
from decimal import Decimal
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from .engine import generate_report
# Create your views here.


def create_report(request):
    """ sample data """
    parsed_data = [
        {
            "nickname": "Bangalilove",
            "player_id": "53015",
            "agent_id": "43333",
            "total_winnings": "-52.56",
            "fee": "1175.35",
            "insurance": "0",
            "jackpot": "0",
            "hands": "127"
        },
        {
            "nickname": "Sammyfarhana",
            "player_id": "57410",
            "agent_id": "43333",
            "total_winnings": "315.39",
            "fee": "1175.35",
            "insurance": "0",
            "jackpot": "0",
            "hands": "893"
        }
    ]
    """ sample agent ID """
    agent_id = 43333

    try:
        agent = Agent.objects.get(club_agent_id=agent_id)
    except Agent.DoesNotExist:
        raise Http404("Agent does not exist")
    generate_report(parsed_data, agent_id=agent_id)
    # todo some validation for accounting
    return HttpResponseRedirect(reverse('index'))
