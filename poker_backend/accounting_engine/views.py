from django.shortcuts import render
from .models import Report
from decimal import Decimal
from django.http import Http404
# Create your views here.

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
agent_id = 43333
user = User.objects.get(pk=2)


def create_report(request):
    #user = request.user
    user = user
    agent = Agent.objects.get(club_agent_id=agent_id)
    for row in parsed_data:
        account_id = row["player_id"]
        try:
            account =
        except Account.DoesNotExist:
            raise Http404("account does not exist")
        total_winnings = Decimal(row["total_winnings"])
        insurance = Decimal(row["insurance"])
        jackpot = Decimal(row["jackpot"])
        hands = int(row["hands"])
        total_rake = Decimal(row["fee"])
        gross_WL = total_winnings + insurance + jackpot
