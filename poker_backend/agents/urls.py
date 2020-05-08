from django.urls import path
from agents import views

urlpatterns = [
    path('', views.createAgent, name="create_agent"),
    #path('api/agent', views.agent, name="agent"),
]
