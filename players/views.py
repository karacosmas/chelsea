from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Person
from .serializers import PersonSerializer

@api_view (["GET"])
def list_players(request):
    
    Players = Person.objects.all()

    serializer = PersonSerializer(Players, many=True)
    content = {
        "Players" : serializer.data,
    }

    return Response(content)


    
# Create your views here.