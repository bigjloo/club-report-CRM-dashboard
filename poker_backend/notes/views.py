from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, Http404, HttpResponse
from notes.serializers import NoteSerializer
from notes.models import Note
from django.core import serializers
from django.urls import reverse
from agents.models import AgentPlayer
import json

""" remove """
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def get_notes(request, agent_id):
    try:
        note = Note.objects.get(agent_player=agent_id)
    except Note.DoesNotExist:
        return Http404("Note retrieve fail")
        #data = serializers.serialize('json', [note], fields='note')
        #json_data = json.dumps(data)
    return HttpResponse(serializers.serialize('json', [note]))


def update_note(request, agent_id):

    if request.method == "POST":
        agent_player = AgentPlayer.objects.get(pk=agent_id)
        note_obj, created = Note.objects.get_or_create(
            agent_player=agent_player)
        note = request.POST['note']
        note_obj.note = note
        note_obj.save()
        return HttpResponseRedirect(reverse('index'))
