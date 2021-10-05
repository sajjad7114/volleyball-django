from rest_framework import viewsets
from .serializers import StadiumSerializer, MatchSerializer
from .models import Stadium, Match
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework import status
from django.shortcuts import get_object_or_404

# Create your views here.


class StadiumViewSet(viewsets.ModelViewSet):
    serializer_class = StadiumSerializer
    queryset = Stadium.objects.all()


class MatchViewSet(viewsets.ModelViewSet):
    serializer_class = MatchSerializer
    queryset = Match.objects.all()
