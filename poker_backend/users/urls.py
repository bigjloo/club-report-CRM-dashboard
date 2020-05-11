from django.urls import path, include
from users import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('', views.index, name="index"),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name="logout"),
    path('create_report', include('accounting_engine.urls')),
    path('create_agent', include('agents.urls')),
    #path('create_player', include('agents.urls')),
    path('create_account', include('agents.urls')),
]
