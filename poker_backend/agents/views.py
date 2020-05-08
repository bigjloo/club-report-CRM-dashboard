from django.shortcuts import render
from .create import createAgent
#from rest_framework import viewsets, permissions
from .serializers import PlayerSerializer, AgentSerializer, AccountSerializer
from django.http import JsonResponse, HttpResponseRedirect
from rest_framework.parsers import FormParser

#
#from django.contrib.auth.models import User
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def createAgent(request):
    user = request.user
    data = FormParser().parse(request)
    serializer = AgentSerializer(data=data)
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


def createAccount(request):
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


# @csrf_exempt
# def agent(request):
#    #user = request.user
#    user = User.objects.get(pk=2)
#    if request.method == "GET":
#        agents = user.agents.all()
#        serializer = AgentSerializer(agents, many=True)
#        return JsonResponse(serializer.data, safe=False)

#    elif request.method == "POST":
#        data = JSONParser().parse(request)
#        serializer = AgentSerializer(data=data)
#        if serializer.is_valid():
#            serializer.save()
#            return JsonResponse(serializer.data, status=201)
#        return JsonResponse(serializer.errors, status=400)
