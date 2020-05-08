from django.urls import path, include
from agents import views

urlpatterns = [
    path('create_agent', views.createAgent, name="create_agent"),
    path('create_player', views.createPlayer, name="create_player"),
    path('create_account', views.createAccount, name="create_account"),
    #path('api/agent', views.agent, name="agent"),
]
