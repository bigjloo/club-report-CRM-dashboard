from django.urls import path
from accounting_engine import views

urlpatterns = [
    path('create_report/', views.create_report_view, name='create_report'),

]

#path('upload_report', views.create_report, name='upload_report'),
