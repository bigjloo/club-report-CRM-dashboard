from django.urls import path, include
from accounting_engine import views
from accounting_engine.views import ReportView, UploadFileView, UploadFileInitialAccountsView


urlpatterns = [
    path('create_report/', views.create_report_view, name='create_report'),

    path('reports/', ReportView.as_view(), name='reports'),
    path('upload_file/', UploadFileView.as_view(), name='upload_file'),
    path('initial_account_load', UploadFileInitialAccountsView.as_view(),
         name='initial_account_load'),
]

#path('upload_report', views.create_report, name='upload_report'),
#path('reports/', views.report_view, name='reports'),
