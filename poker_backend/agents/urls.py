from django.urls import path
from agents import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('create_agent/', views.AgentPlayerList.as_view(), name="create_agent"),
    path('agent_player/<int:pk>/', views.AgentPlayerDetail.as_view(),
         name="agent_player_detail"),
    path('create_account', views.create_account, name="create_account"),


]

urlpatterns = format_suffix_patterns(urlpatterns)
