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
        agent_player = request.user.agent_players.objects.get(
            pk=agent_id)
        note = Note.objects.get(pk=agent_player.note.pk).note
    except Note.DoesNotExist:
        return Http404("Note retrieve fail")
        #data = serializers.serialize('json', [note], fields='note')
        #json_data = json.dumps(data)
    return HttpResponse(serializers.serialize('json', [note]))


def update_note(request, agent_id):

    if request.method == "POST":
        try:
            agent_player = request.user.agent_players.objects.get(pk=agent_id)
        except AgentPlayer.DoesNotExist:
            return Http404("Agent Does not exist")
        if agent_player.note is not None:
            agent_player.note.note = request.POST['note']
            agent_player.note.save()
        else:
            agent_player.note = Note(note=request.POST['note'])
            agent_player.note.save()
        return HttpResponseRedirect(reverse('index'))
