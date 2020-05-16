from django.shortcuts import render
from .models import Report
from django.contrib.auth.models import User
from decimal import Decimal
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .engine import generate_report
from agents.models import Account, AgentPlayer, Club
from .serializers import ReportSerializer
from rest_framework.parsers import JSONParser
# Create your views here.

json_sample = [
    {
        "club": 21872,
        "nickname": "Bangalilove",
        "account": 53015,
        "agent_player": 43333,
        "gross_winloss": -52.56,
        "total_rake": 1175.35,
        "insurance": 0,
        "jackpot": 0,
        "hands": 127,
    },
    {
        "club": 21872,
        "nickname": "Sammyfarhana",
        "account": 57410,
        "agent_player": 43333,
        "gross_winloss": 315.39,
        "total_rake": 1175.35,
        "insurance": 0,
        "jackpot": 0,
        "hands": 893
    }
]

parsed_data2 = [
    {
        "club": 21872,
        "nickname": "rundlemall",
        "account": 43003,
        "agent_player": "Tim",
        "gross_winloss": 364.92,
        "total_rake": 273.57,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 21872,
        "nickname": "HG",
        "account": 43260,
        "agent_player": "Tim",
        "gross_winloss": -10,
        "total_rake": 1.41,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 21872,
        "nickname": "Pokerlovrr",
        "account": 53002,
        "agent_player": "Tim",
        "gross_winloss": -1615.79,
        "total_rake": 781.85,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 21872,
        "nickname": "monstermong",
        "account": 338570,
        "agent_player": "Tim",
        "gross_winloss": -240,
        "total_rake": 24,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 21872,
        "nickname": "SellsAlmonds",
        "account": 47095,
        "agent_player": "Justin",
        "gross_winloss": -80,
        "total_rake": 8,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 21872,
        "nickname": "Sammyfarhana",
        "account": 57410,
        "agent_player": "Justin",
        "gross_winloss": -212.79,
        "total_rake": 70.26,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 21872,
        "nickname": "UpToYou",
        "account": 60682,
        "agent_player": "Justin",
        "gross_winloss": -752.26,
        "total_rake": 91.25,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 21872,
        "nickname": "ajibhailated",
        "account": 61126,
        "agent_player": "Justin",
        "gross_winloss": 446.99,
        "total_rake": 54.08,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 21872,
        "nickname": "Pluribush",
        "account": 64002,
        "agent_player": "Justin",
        "gross_winloss": 28.66,
        "total_rake": 153.13,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 21872,
        "nickname": "Yam9You",
        "account": 64003,
        "agent_player": "Justin",
        "gross_winloss": 127.54,
        "total_rake": 14.15,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 21872,
        "nickname": "FcklFknAunty",
        "account": 64148,
        "agent_player": "Justin",
        "gross_winloss": 250.24,
        "total_rake": 8,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 21872,
        "nickname": "IkanPaus",
        "account": 64157,
        "agent_player": "Justin",
        "gross_winloss": 137.01,
        "total_rake": 8,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 21872,
        "nickname": "Imthebest",
        "account": 73086,
        "agent_player": "Justin",
        "gross_winloss": -451.9,
        "total_rake": 149.17,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 21872,
        "nickname": "omahasama",
        "account": 310823,
        "agent_player": "Justin",
        "gross_winloss": 0,
        "total_rake": 0,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 21872,
        "nickname": "rubyrabbit",
        "account": 366550,
        "agent_player": "Tim",
        "gross_winloss": -155.06,
        "total_rake": 142,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 21872,
        "nickname": "jacks888",
        "account": 237096,
        "agent_player": "Justin",
        "gross_winloss": 308.14,
        "total_rake": 50.6,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 727588,
        "nickname": "Dyn0mit3",
        "account": 38648,
        "agent_player": "Justin",
        "gross_winloss": -70.59,
        "total_rake": 18,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 727588,
        "nickname": "Dygen0rat3",
        "account": 48757,
        "agent_player": "Justin",
        "gross_winloss": -180,
        "total_rake": 18,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 727588,
        "nickname": "Dysc0stu",
        "account": 311339,
        "agent_player": "Justin",
        "gross_winloss": -180,
        "total_rake": 18,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 949733,
        "nickname": "Dyn0mit3",
        "account": 38648,
        "agent_player": "Justin",
        "gross_winloss": -150,
        "total_rake": 15,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 949733,
        "nickname": "Dygen0rat3",
        "account": 48757,
        "agent_player": "Justin",
        "gross_winloss": -150,
        "total_rake": 15,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 949733,
        "nickname": "Dysc0stu",
        "account": 311339,
        "agent_player": "Justin",
        "gross_winloss": -150,
        "total_rake": 15,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 22093,
        "nickname": "1outking",
        "account": 373566,
        "agent_player": "Tim",
        "gross_winloss": 52.53,
        "total_rake": 37.5,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    },
    {
        "club": 22093,
        "nickname": "remmington12",
        "account": 404264,
        "agent_player": "Tim",
        "gross_winloss": 1394.66,
        "total_rake": 56.5,
        "insurance": "",
        "jackpot": "",
        "hands": ""
    }
]


def create_report_view(request):
    json_data = parsed_data2
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
            account = Account.objects.get(club_account_id=club_account_id)
        except Account.DoesNotExist:
            raise Http404("Account does not exist")
        serializer = ReportSerializer(data=row)
        if serializer.is_valid():
            report = serializer.save()
            report.agent_player = agent_player
            report.account = account
            report.club = club
            report.save()
        else:
            print(serializer.errors)
            raise Http404("serializer not valid")
    return HttpResponseRedirect(reverse('index'))


def create_report_view3(request):
    json_data = json_sample
    for row in json_data:
        try:
            agent_player_id = int(row.pop('agent_player'))
            agent_player = AgentPlayer.objects.get(code=agent_player_id)
        except AgentPlayer.DoesNotExist:
            raise Http404
        try:
            club_id = int(row.pop('club'))
            club = Club.objects.get(club_id=club_id)
        except Club.DoesNotExist:
            raise Http404
        try:
            club_account_id = int(row.pop('account'))
            account = Account.objects.get(club_account_id=club_account_id)
        except Account.DoesNotExist:
            raise Http404
        serializer = ReportSerializer(data=row)
        if serializer.is_valid():
            report = serializer.save()
            report.agent_player = agent_player
            report.account = account
            report.club = club
            report.save()
        else:
            print(serializer.errors)
            raise Http404("serializer not valid")
    return HttpResponseRedirect(reverse('index'))


def create_report_view2(request):
    """ sample data """
    json_sample = [
        {
            "club": 21872,
            "nickname": "Bangalilove",
            "account": 53015,
            "agent_player": 43333,
            "gross_winloss": -52.56,
            "total_rake": 1175.35,
            "insurance": 0,
            "jackpot": 0,
            "hands": 127,
        },
        {
            "club": 21872,
            "nickname": "Sammyfarhana",
            "account": 57410,
            "agent_player": 43333,
            "gross_winloss": 315.39,
            "total_rake": 1175.35,
            "insurance": 0,
            "jackpot": 0,
            "hands": 893
        }
    ]

    if request.method == 'GET':

        json_data = json_sample
        for row in json_data:
            try:
                agent_player_id = int(row.pop('agent_player'))
                agent_player = AgentPlayer.objects.get(code=agent_player_id)
            except AgentPlayer.DoesNotExist:
                raise Http404
            try:
                club_id = int(row.pop('club'))
                club = Club.objects.get(club_id=club_id)
            except Club.DoesNotExist:
                raise Http404
            try:
                club_account_id = int(row.pop('account'))
                account = Account.objects.get(club_account_id=club_account_id)
            except Account.DoesNotExist:
                raise Http404
            serializer = ReportSerializer(data=row)
            if serializer.is_valid():
                report = serializer.save()
                report.agent_player = agent_player
                report.account = account
                report.club = club
                report.save()
            else:
                print(serializer.errors)
                raise Http404("serializer not valid")
        return HttpResponseRedirect(reverse('index'))
