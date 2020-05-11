from django.urls import path, include
from agents import views

urlpatterns = [
    path('create_agent', views.create_agent_player, name="create_agent"),
    path('create_account', views.create_account, name="create_account"),

]
