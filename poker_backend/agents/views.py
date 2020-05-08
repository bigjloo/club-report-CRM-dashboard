from django.shortcuts import render
from .create import createAgent
#from rest_framework import viewsets, permissions
from .serializers import PlayerSerializer, AgentSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
#
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def createAgent(request):
    user = request.user
    club = Club.objects.get(pk=1)
    data = {
        "nickname": "brobro",
        "club_agent_id": "898989",
        "club": "1",
        "rakeback": "0.55",
    }
    serializer = AgentSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user=user)
        return JsonResponse(serializer.data, status=201)
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
