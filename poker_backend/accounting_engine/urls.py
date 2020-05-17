from django.urls import path
from accounting_engine import views
from accounting_engine.views import ReportView


urlpatterns = [
    path('create_report/', views.create_report_view, name='create_report'),

    path('reports/', ReportView.as_view(), name='reports'),
]

#path('upload_report', views.create_report, name='upload_report'),
#path('reports/', views.report_view, name='reports'),
