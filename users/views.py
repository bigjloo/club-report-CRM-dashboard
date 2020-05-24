from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse
from agents.models import Club, AgentPlayer
from .forms import AgentPlayerForm, AccountForm, AccountClubForm, UserForm, UploadFileForm, EditAccountForm, AddClubForm
from rest_framework import generics
from notes.models import Announcement

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    user = request.user
    clubs = Club.objects.all()
    agent_player_form = AgentPlayerForm()
    account_form = AccountForm(user)
    upload_form = UploadFileForm()
    account_club_form = AccountClubForm(user)
    edit_account_form = EditAccountForm(user)
    add_club_form = AddClubForm()
    announcements = Announcement.objects.all()
    context = {
        "user": user,
        "clubs": clubs,
        "agent_form": agent_player_form,
        "account_form": account_form,
        'upload_form': upload_form,
        'account_club_form': account_club_form,
        'edit_account_form': edit_account_form,
        'add_club_form': add_club_form,
        'announcements': announcements,
    }
    return render(request, "users/user.html", context)


def get_account_club_form(request, agent_id):
    try:
        agent_player = AgentPlayer.objects.get(pk=agent_id)
    except Agent.DoesNotExist:
        return Http404("Agent Does Not Exist")
    account_club_form = AccountClubForm(agent_player)
    return HttpResponse("get club form")


def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'users/login.html', {"message": "Error: Cannot log in."})


def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {"message": "Logged out"})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


"""
def register(request):
    if request.method == "POST":
        # create user
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        user = authenticate(request, username=username,
                            password=password, email=email)
        if user is not None:
            new_user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            new_user.save()
            return render(request, 'users/login.html')
        else:
            return HttpResponseRedirect(reverse('register'), {"message": "Registration Failed"})
    context = {
        'form': UserForm()
    }

    return render(request, 'users/register.html', context)
"""


def guide(request):
    user = request.user
    load_account_form = UploadFileForm()
    agent_player_form = AgentPlayerForm()
    account_form = AccountForm(user)
    upload_form = UploadFileForm()

    context = {
        'load_account_form': load_account_form,
        "agent_form": agent_player_form,
        "account_form": account_form,
        'upload_form': upload_form,
    }
    return render(request, 'users/guide.html', context)
