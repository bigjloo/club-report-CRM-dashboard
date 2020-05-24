from django.shortcuts import render, redirect
from .models import Report
from django.contrib.auth.models import User
from decimal import Decimal
from django.http import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from .engine import get_report, csvfile_to_json, process_report, calculate_user_statement, process_initial_account_load
from agents.models import Account, AgentPlayer, Club
from .serializers import ReportSerializer
from rest_framework.parsers import JSONParser, FormParser, FileUploadParser
from .forms import DateForm
from django.views import View
from users.forms import UploadFileForm
import csv
import json
from rest_framework.views import APIView
from users.forms import AccountForm, AgentPlayerForm, UploadFileForm
# Create your views here.


class UploadFileInitialAccountsView(View):
    def post(self, request):
        csvfile = request.FILES['file']
        json_data = csvfile_to_json(csvfile)
        accounts = process_initial_account_load(json_data)
        # add notification for success or fail + accounts list
        return redirect('index')


class UploadFileView(View):
    def post(self, request):
        csvfile = request.FILES['file']
        # if not csvfile.endswith('.csv'):
        #    return Http404("File not csv type")
        json_data = csvfile_to_json(csvfile)
        process_report(json_data)
        return redirect('reports')


class ReportView(View):
    def post(self, request):
        form = DateForm(request.POST)
        if form.is_valid():
            user = request.user
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            reports = get_report(start_date, end_date, user)
            user_statement = calculate_user_statement(reports, user)
            user_earnings = user_statement['user_total_earnings']
            agent_player_statement = user_statement['agent_player_statement']
            club_statement = user_statement['club_statement']
            agent_player_form = AgentPlayerForm()
            account_form = AccountForm(user)
            upload_form = UploadFileForm()
            context = {
                'form': DateForm(),
                'reports': reports,
                "agent_form": agent_player_form,
                "account_form": account_form,
                'upload_form': upload_form,
                'user_earnings': user_earnings,
                'agent_player_statement': agent_player_statement,
                'club_statement': club_statement,
            }

            return render(request, 'reports/reports.html', context)

    def get(self, request):
        form = DateForm()
        return render(request, 'reports/reports.html', {'form': form})


def create_report_view(request):
    process_report(json_data)
    return HttpResponseRedirect(reverse('index'))


def report_view(request):
    form = DateForm()
    return render(request, 'reports/reports.html', {'form': form})
