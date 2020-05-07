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
    # AgentReport counter
    agent_gross_winloss = 0
    agent_total_rake = 0
    agent_rakeback_earnings = 0
    agent_net_winloss = 0
    agent_jackpot = 0
    agent_insurance = 0
    agent_hands = 0

    # create account report
    for row in parsed_data:
        account_id = row["player_id"]
        # check if account exist in database
        try:
            account = Account.objects.get(club_account_id=account_id)
        except Account.DoesNotExist:
            raise Http404("account does not exist")
        # get data from parsed_data
        total_winnings = Decimal(row["total_winnings"])
        insurance = Decimal(row["insurance"])
        jackpot = Decimal(row["jackpot"])
        hands = int(row["hands"])
        total_rake = Decimal(row["fee"])
        # calculate engine
        gross_winloss = total_winnings
        rakeback_earnings = account.rakeback * total_rake
        net_winloss = gross_winloss + rakeback_earnings + insurance + jackpot
        # create AccountReport
        try:
            account_report = AccountReport(gross_winloss=gross_winloss, total_rake=total_rake, rakeback_earnings=rakeback_earnings,
                                           net_winloss=net_winloss, insurance=insurance, jackport=jackpot, hands=hands, account=account)
        except:
            raise Http404("error creating account report")
        account_report.save()
        agent_rakeback_from_account = ((agent.rakeback *
                                        total_rake) - (rakeback_earnings))
        # sum all row data for agent total
        agent_gross_winloss += gross_winloss
        agent_total_rake += total_rake
        agent_rakeback_earnings += agent_rakeback_from_account
        agent_net_winloss += (net_winloss + agent_rakeback_from_account)
        agent_jackpot += jackpot
        agent_insurance += insurance
        agent_hands += hands

    #user = request.user
    user = user
    #agent = request.data.agent_id
    agent = Agent.objects.get(club_agent_id=agent_id)
    # create AgentReport
    try:
        agent_report = AgentReport(gross_winloss=agent_gross_winloss,
                                   total_rake=agent_total_rake, rakeback_earnings=agent_rakeback_earnings, net_winloss=agent_net_winloss, insurance=agent_insurance, jackpot=agent_jackpot, hands=agent_hands, agent=agent)
    except:
        raise Http404("error creating agent report")
    agent_report.save()
    # some validation for accounting
