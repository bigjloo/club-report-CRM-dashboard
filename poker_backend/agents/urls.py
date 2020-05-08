from django.urls import path
from agents import views

urlpatterns = [
    path('create_agent', views.createAgent, name="create_agent")
]
