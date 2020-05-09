from agents.models import Account, Agent
from decimal import Decimal
from django.http import Http404
from accounting_engine.models import AccountReport, AgentReport


def calculate_account_rakeback(rakeback_percent, rake):
    account_rakeback = round((rakeback_percent * rake), 2)
    return account_rakeback


def calculate_account_net_winloss(gross_winloss, rakeback_earnings, insurance, jackpot):
    account_net_winloss = round(
        (gross_winloss + rakeback_earnings + insurance + jackpot), 2)
    return account_net_winloss


def calculate_agent_rakeback(agent_rakeback_percent, rake, account_rakeback):
    agent_rakeback = round(
        ((agent_rakeback_percent * rake) - account_rakeback), 2)
    return agent_rakeback


def generate_report(data, agent_id):
    agent = Agent.objects.get(club_agent_id=agent_id)
    agent_gross_winloss = 0
    agent_total_rake = 0
    agent_rakeback_earnings = 0
    agent_net_winloss = 0
    agent_jackpot = 0
    agent_insurance = 0
    agent_hands = 0
    for row in data:
        account_id = row["player_id"]
        try:
            account = Account.objects.get(club_account_id=account_id)
        except Account.DoesNotExist:
            raise Http404("account does not exist")

        gross_winloss = Decimal(row["total_winnings"])
        insurance = Decimal(row["insurance"])
        jackpot = Decimal(row["jackpot"])
        hands = int(row["hands"])
        total_rake = Decimal(row["fee"])
        rakeback_earnings = calculate_account_rakeback(
            rakeback_percent=account.rakeback,
            rake=total_rake
        )
        net_winloss = calculate_account_net_winloss(
            gross_winloss,
            rakeback_earnings,
            insurance,
            jackpot
        )

        try:
            account_report = AccountReport(
                gross_winloss=gross_winloss,
                total_rake=total_rake,
                rakeback_earnings=rakeback_earnings,
                net_winloss=net_winloss,
                insurance=insurance,
                jackpot=jackpot,
                hands=hands,
                account=account
            )
        except:
            raise Http404("error creating account report")
        account_report.save()
        agent_rakeback_from_account = calculate_agent_rakeback(
            agent_rakeback_percent=agent.rakeback,
            rake=total_rake,
            account_rakeback=rakeback_earnings
        )

        agent_gross_winloss += gross_winloss
        agent_total_rake += total_rake
        agent_rakeback_earnings += agent_rakeback_from_account
        agent_net_winloss += (net_winloss + agent_rakeback_from_account)
        agent_jackpot += jackpot
        agent_insurance += insurance
        agent_hands += hands
    try:
        agent_report = AgentReport(
            gross_winloss=agent_gross_winloss,
            total_rake=agent_total_rake,
            rakeback_earnings=agent_rakeback_earnings,
            net_winloss=agent_net_winloss,
            insurance=agent_insurance,
            jackpot=agent_jackpot,
            hands=agent_hands,
            agent=agent
        )
    except:
        raise Http404("error creating agent report")
    agent_report.save()
