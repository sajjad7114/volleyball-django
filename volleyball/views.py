from rest_framework import viewsets
from .serializers import StadiumSerializer, MatchSerializer, TransActionSerializer
from .models import Stadium, Match, TransAction
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
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


class TransActionAPIView(APIView):
    def get(self, request, uid):
        try:
            user = User.objects.get(pk=uid)
            transactions = user.transaction_set.all()
            serializer = TransActionSerializer(transactions, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, uid):
        serializer = TransActionSerializer(data=request.data)
        serializer.initial_data['user'] = uid

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransActionDetails(APIView):
    def get(self, request, uid, pk):
        try:
            user = User.objects.get(pk=uid)
            transaction = user.transaction_set.get(pk=pk)
            serializer = TransActionSerializer(transaction)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

