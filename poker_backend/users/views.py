from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.urls import reverse
from agents.models import Club, AgentPlayer
from .forms import AgentPlayerForm, AccountForm, AccountClubForm

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    user = request.user
    clubs = Club.objects.all()
    agent_player_form = AgentPlayerForm()
    account_form = AccountForm(user)
    account_club_form = AccountClubForm()
    context = {
        "user": request.user,
        "clubs": clubs,
        "agent_form": agent_player_form,
        "account_form": account_form,
        'account_club_form': account_club_form
    }
    return render(request, "users/user.html", context)


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
    return render(request, 'users/register.html')
