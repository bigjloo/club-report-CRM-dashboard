from django.urls import path
from agents import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('create_agent/', views.AgentPlayerList.as_view(), name="create_agent"),
    path('agent_player/<int:pk>/', views.AgentPlayerDetail.as_view(),
         name="agent_player_detail"),
    path('create_account', views.create_account, name="create_account"),
    path('api/accounts/', views.AccountList.as_view(), name='api_accounts'),
    path('accounts/', views.accounts, name='accounts'),
    path('account/<int:pk>', views.AccountDetail.as_view(), name="account_detail"),
    path('add_club/', views.add_club, name="add_club"),
    path('account_clubs/<int:account_id>', views.get_clubs, name="get_clubs")

]

urlpatterns = format_suffix_patterns(urlpatterns)
