from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, Http404, HttpResponse
from notes.serializers import NoteSerializer
from notes.models import Note
from django.core import serializers
import json

""" remove """
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


@csrf_exempt
def get_notes(request):
    if request.method == "POST":
        agent_pk = request.POST['agent_id']
        try:
            note = Note.objects.get(agent_player=agent_pk)
        except Note.DoesNotExist:
            return Http404("Note retrieve fail")
        #data = serializers.serialize('json', [note], fields='note')
        #json_data = json.dumps(data)

        return HttpResponse(serializers.serialize('json', [note]))
