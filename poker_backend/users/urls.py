from django.urls import path, include
from users import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name="logout"),
    path('create_agent/', include('agents.urls')),
    path('create_account/', include('agents.urls')),
    path('', include('accounting_engine.urls')),
]

#path('upload_report', include('accounting_engine.urls')),
"""  
 rest framework tutorial
"""
#path('user/', views.UserList.as_view()),
#path('user/<int:pk>/', views.UserDetail.as_view()),
#path('api-auth/', include('rest_framework.urls')),
#path('', include('accounting_engine.urls')),
