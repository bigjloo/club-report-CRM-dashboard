from agents.models import Account, AgentPlayer, Club
from decimal import Decimal
from django.http import Http404
from accounting_engine.models import Report
from .serializers import ReportSerializer
import json
import csv
from django.core.exceptions import ValidationError
from agents.serializers import InitialAccountSerializer
"""
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
"""


def validate_agent_player(agent_player_id):
    try:
        agent_player = AgentPlayer.objects.get(code=agent_player_id)
    except AgentPlayer.DoesNotExist:
        raise Http404("Agent does not exist")
    return agent_player


def get_report(start_date, end_date, user):
    reports = {}
    try:
        agent_players = user.agent_players.all()
    except AgentPlayer.DoesNotExist:
        return Http404('Error retrieving agent players')
    for agent_player in agent_players:
        agent_player_reports = agent_player.reports.filter(
            created__range=[start_date, end_date])
        reports[f'{agent_player}'] = agent_player_reports
    return reports


def csvfile_to_json(file):
    json_data = []
    rows = []
    # convert bytes to strings
    for row in file:
        cleaned_row = row.decode('UTF-8').rstrip('\r\n')
        rows.append(cleaned_row)
    headers = rows.pop(0).split(',')
    number_of_columns = len(headers)
    number_of_rows = len(rows)
    for i in range(number_of_rows):
        record = {}
        current_row = rows[i].split(',')
        for j in range(number_of_columns):
            record[headers[j]] = current_row[j]
        json_data.append(record)
    return json_data


def process_report(json_data, user):
    reports = []
    for row in json_data:
        try:
            agent_player_id = row.pop('agent_player')
            agent_player = AgentPlayer.objects.get(code=agent_player_id)
        except AgentPlayer.DoesNotExist:
            raise Http404("Agent does not exist")
        try:
            club_id = row.pop('club')
            club = Club.objects.get(club_id=club_id)
        except Club.DoesNotExist:
            raise Http404("Club does not exist")
        try:
            club_account_id = row.pop('account')
            account = Account.objects.get(
                club_account_id=club_account_id, user=user)
        except Account.DoesNotExist:
            raise Http404("Account does not exist")
        serializer = ReportSerializer(data=row)
        if serializer.is_valid():
            report = serializer.save()
            club_deal = account.club_deal.get(club=club)
            report.rakeback = club_deal.rakeback_percentage * report.total_rake
            report.net_winloss = report.gross_winloss + report.rakeback
            report.net_winloss_fiat = club_deal.chip_value * report.net_winloss
            report.agent_player = agent_player
            report.account = account
            report.club = club
            # eport.save()
            reports.append(report)
        else:
            print(serializer.errors)
            raise Http404("serializer not valid")

    for r in reports:
        r.save()
    return reports


def process_initial_account_load(json_data, user):
    accounts = []
    for row in json_data:
        serializer = InitialAccountSerializer(data=row)
        if serializer.is_valid():
            account = serializer.save(user=user)
            accounts.append(account)
        else:
            print(serializer.errors)
            raise Http404("serializer not valid")

    return accounts


def calculate_user_statement(reports, user):
    user_total_earnings = Decimal(0)
    user_club_deal = {}
    club_statement = {}
    for club_deal in user.club_deals.all():
        user_club_deal[club_deal.club_id] = {
            'rakeback': club_deal.rakeback_percentage, 'chip_value': club_deal.chip_value}
        club_statement[club_deal.club.name] = Decimal(0)
    agent_player_statement = {}
    for agent_player, reports in reports.items():
        agent_player_statement[agent_player] = Decimal(0)
        for report in reports:
            # print(report.account)
            account_total_rakeback = (report.total_rake *
                                      user_club_deal[report.club.id]['rakeback'] *
                                      user_club_deal[report.club.id]['chip_value'])
            #print(f"account total rakeback = {account_total_rakeback}")
            account_rakeback_out = (report.rakeback *
                                    report.account.club_deal.first().chip_value)
            #print(f"account rakeback out = {account_rakeback_out}")
            earnings = account_total_rakeback - account_rakeback_out
            #print(f"user earnings = {earnings}")
            user_total_earnings += earnings
            agent_player_statement[agent_player] += report.net_winloss_fiat
            # print(
            #    f"agent_player_statement {agent_player}= {agent_player_statement[agent_player]}")
            club_statement[report.club.name] += ((report.gross_winloss + (report.total_rake * user_club_deal[report.club.id]['rakeback']))
                                                 * user_club_deal[report.club.id]['chip_value'])
            # print(
            #    f"club statement {report.club.name} = {club_statement[report.club.name]}")

    user_statement = {}
    user_statement['user_total_earnings'] = user_total_earnings
    user_statement['agent_player_statement'] = agent_player_statement
    user_statement['club_statement'] = club_statement
    return user_statement


def prepare_statement(reports, user):
    TODO


"""
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
            account_report = Report(
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
"""
