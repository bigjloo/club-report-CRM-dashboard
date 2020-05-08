from django.shortcuts import render
from create import createAgent

# Create your views here.


def createAgent(request):
    user_id = request.user.id

    data = {
        "nickname": "Brodash",
        "club_agent_id": "898989",
        "club_id": "1",
        "rakeback" = "0.55",
    }

    createAgent(data, user_id)
    return jsonify({"success": True, "message": "New account created"})
