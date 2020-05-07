from django.urls import path
from accounting_engine import views

urlpatterns = [
    path('create_report', views.create_report, name='create_report'),
]
