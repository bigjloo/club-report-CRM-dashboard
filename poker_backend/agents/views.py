from django.shortcuts import render
from .create import createAgent
#from rest_framework import viewsets, permissions
from .serializers import AgentPlayerSerializer, AccountSerializer
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.parsers import FormParser

#
#from django.contrib.auth.models import User
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def create_agent_player(request):
    user = request.user
    data = FormParser().parse(request)
    serializer = AgentPlayerSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user=user)
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next, status=201)
    return JsonResponse(serializer.errors, status=400)


def createPlayer(request):
    user = request.user
    data = FormParser().parse(request)
    serializer = PlayerSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user=user)
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next, status=201)
    return JsonResponse(serializer.errors, status=400)


def create_account(request):
    data = FormParser().parse(request)
    serializer = AccountSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next, status=201)
    return JsonResponse(serializer.errors, status=400)


"""
class AgentViewSet(viewsets.ModelViewSet):
     
    #API endpoint that allows Agent to be viewed or edited
   
    # for tutorial. for app, set restrictions to user.agents only
    queryset = Agent.objects.all()

    serializer_class = AgentSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]
"""
