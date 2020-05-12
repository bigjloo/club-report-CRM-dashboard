from django.shortcuts import render
from .create import createAgent
#from rest_framework import viewsets, permissions
from .serializers import AgentPlayerSerializer, AccountSerializer
from django.http import JsonResponse, HttpResponseRedirect, Http404
from rest_framework.parsers import FormParser
from agents.models import AccountClub, AgentPlayer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from .permissions import isOwnerOrReadOnly

#
#from django.contrib.auth.models import User
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.

"""
@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def create_agent_player(request):
    user = request.user
    if request.method == 'POST':
        serializer = AgentPlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""


class AgentPlayerList(generics.ListCreateAPIView):
    queryset = AgentPlayer.objects.all()
    serializer_class = AgentPlayerSerializer
    # permission_classes = [
    #    permissions.IsAuthenticatedOrReadOnly, isOwnerOrReadOnly]
    # add permission class here

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


# not tested yet
class AgentPlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgentPlayer.objects.all()
    serializer_class = AgentPlayerSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        user = self.request.user
        return AgentPlayer.objects.filter(user=user)


"""
    def get(self, request, format=None):
        user = request.user
        agent_players = AgentPlayer.objects.get(user=user)
        serializer = AgentPlayerSerializer(agent_players, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        user = request.user
        serializer = AgentPlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""


class AgentPlayerDetail(APIView):
    """
    Retrieve, update or delete a snippet instance
    """

    def get_object(self, pk):
        try:
            return AgentPlayer.objects.get(pk=pk)
        except AgentPlayer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        agent_player = self.get_object(pk)
        serializer = AgentPlayerSerializer(agent_player)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        agent_player = self.get_object(pk)
        serializer = AgentPlayerSerializer(agent_player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        agent_player = self.get_object(pk)
        agent_player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
def create_agent_player(request):
    user = request.user
    data = FormParser().parse(request)
    serializer = AgentPlayerSerializer(data=data)
    if serializer.is_valid():
        serializer.save(user=user)
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next, status=201)
    return JsonResponse(serializer.errors, status=400)
"""


def create_account(request):
    data = FormParser().parse(request)
    rakeback = data.rakeback_percentage
    chip_value = data.chip_value
    account_data = {
        'nickname': data.nickname,
        'club_account_id': data.club_account_id,
    }

    serializer = AccountSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        # account_club = AccountClub(account=serializer.)
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next, status=201)
    return JsonResponse(serializer.errors, status=400)


# @api_view(['POST'])
# def create_account(request):
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
