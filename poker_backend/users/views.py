from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, 'users/login.html')
    context = {
        "user": request.user
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
        return render(request, 'users/login.html', {"message": "error cannot log in"})


def logout_view(request):
    logout(request)
    return render(request, 'users/login.html', {"message": "logged out"})


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
                username=username, password=password, email=email)
            new_user.save()
            return render(request, 'users/login.html')
        else:
            return HttpResponseRedirect(reverse('register', {"message": "Registration Failed"}))
    return render(request, 'users/register.html')
