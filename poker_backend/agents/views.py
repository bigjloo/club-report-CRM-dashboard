from django.shortcuts import render, redirect
from .create import createAgent
# from rest_framework import viewsets, permissions
from .serializers import AgentPlayerSerializer, CreateAccountSerializer, AccountClubSerializer, AccountSerializer
from django.http import JsonResponse, HttpResponseRedirect, Http404
from rest_framework.parsers import FormParser
from agents.models import AccountClub, AgentPlayer, Club, Account
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.views import APIView
from .permissions import isOwnerOrReadOnly
from users.forms import AccountForm
from django.urls import reverse
from users.forms import AccountClubForm

#
# from django.contrib.auth.models import User
# from django.views.decorators.csrf import csrf_exempt

# Create your views here.


class AgentPlayerList(generics.ListCreateAPIView):
    queryset = AgentPlayer.objects.all()
    serializer_class = AgentPlayerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        isOwnerOrReadOnly,
    ]
    # add permission class here

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


# not tested yet
class AgentPlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AgentPlayer.objects.all()
    serializer_class = AgentPlayerSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        isOwnerOrReadOnly,
    ]

    def get_queryset(self):
        user = self.request.user
        return AgentPlayer.objects.filter(user=user)


class AgentPlayerDetail(APIView):
    """
    Retrieve, update or delete an AgentPlayer instance
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


""" put not tested // returns agents of clubs as well """


class AccountDetail(APIView):
    """
    Retrieve, update or delete an Account instance
    """

    def get_object(self, pk):
        try:
            return Account.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        account = self.get_object(pk)
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        account = self.get_object(pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


""" /accounts/"""


def accounts(request):
    if request.method == 'GET':
        user = request.user
        agent_players = AgentPlayer.objects.filter(user=user)
        form = AccountClubForm()
        context = {
            'agent_players': agent_players,
            'form': form,
        }

        return render(request, 'accounts/accounts.html', context)


"""tested. returns json of accounts """


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        isOwnerOrReadOnly,
    ]
    # add permission class here

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


""" in use """


def create_account(request):
    if request.method == 'POST':
        data = FormParser().parse(request)
        serializer = CreateAccountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            next = request.POST.get('next', '/')
            return redirect('index')
        return JsonResponse(serializer.errors, status=400)


""" add club """


def add_club(request):
    if request.method == 'POST':
        data = FormParser().parse(request)
        serializer = AccountClubSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponseRedirect(reverse('accounts'))
        return JsonResponse(serializer.errors, status=400)
