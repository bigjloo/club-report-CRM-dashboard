from django.urls import path
from notes import views

urlpatterns = [
    path('get_notes/<int:agent_id>', views.get_notes, name="get_notes"),
    path('notes/<int:agent_id>', views.update_note, name="update_note"),
]
