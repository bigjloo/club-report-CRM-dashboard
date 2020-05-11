from agents.models import Account, AgentPlayer
from decimal import Decimal
from django.http import Http404

"""
sample agent data:
data = {
    "nickname": "BROBRO",
    "club_agent_id": "898989",
    "club_id": "1",
    "rakeback" = "0.55", 
}

"""


def createAgent(data, user_id):

    nickname = data["nickname"]
    club_agent_id = int(data["club_agent_id"])
    club_id = int(data["club"])
    rakeback = Decimal(data["rakeback"])
    # user= request.user
    user = User.objects.get(pk=user_id)
    try:
        club = Club.objects.get(pk=club_id)
        # todo cannot create agent in same club
        agent = Agent(nickname=nickname,
                      club_agent_id=club_agent_id, club=club, rakeback=rakeback, user=user)
    except Club.DoesNotExist:
        raise Http404("Club does not exist")
    except KeyError:
        raise Http404("KeyError")


# def createAccount(data):
    # TODO here


# def createPlayer(data):
#    # TODO here
