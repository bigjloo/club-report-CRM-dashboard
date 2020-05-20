from django.urls import path
from notes import views

urlpatterns = [
    path('get_notes/', views.get_notes, name="get_notes")
]
