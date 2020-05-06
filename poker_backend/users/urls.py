from django.urls import path
from users import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('', views.index, name="index"),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name="logout"),
]
