from django.urls import path
from balance import views

urlpatterns = [
    path('transaction', views.transaction, name="transaction"),
]
