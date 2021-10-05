import datetime
from rest_framework import viewsets
from .serializers import StadiumSerializer, MatchSerializer, TransActionSerializer, SeatSerializer
from .models import Stadium, Match, Seat
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class StadiumViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = StadiumSerializer
    queryset = Stadium.objects.all()


class MatchViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    serializer_class = MatchSerializer
    queryset = Match.objects.all()


class TransActionAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, uid):
        try:
            user = User.objects.get(pk=uid)
            if user != self.request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            transactions = user.transaction_set.all()
            serializer = TransActionSerializer(transactions, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request, uid):
        serializer = TransActionSerializer(data=request.data)
        serializer.initial_data['user'] = uid
        if uid != self.request.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransActionDetails(APIView):
    def get(self, request, uid, pk):
        try:
            user = User.objects.get(pk=uid)
            if user != self.request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            transaction = user.transaction_set.get(pk=pk)
            serializer = TransActionSerializer(transaction)
            res = serializer.data.copy()
            try:
                res['seat'] = transaction.seat.pk
            except:
                res['seat'] = None
            return Response(res)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class TicketAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, uid):
        try:
            user = User.objects.get(pk=uid)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if user != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        seats = user.seat_set.all()
        serializer = SeatSerializer(seats, many=True)
        return Response(serializer.data)

    def post(self, request, uid):
        try:
            user = User.objects.get(pk=uid)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if user != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        serializer = SeatSerializer(data=request.data)
        serializer.initial_data['user'] = uid

        if serializer.is_valid():
            match = serializer.validated_data['match']
            index = serializer.validated_data['index']
            transaction = serializer.validated_data['transaction']
            available_list = match.available_list()
            if index not in available_list:
                return Response({'message': 'The place is unavailable'}, status=status.HTTP_403_FORBIDDEN)
            if match.date < datetime.date.today():
                return Response({'message': 'The match is done'}, status=status.HTTP_410_GONE)
            if transaction.amount < match.ticket_price:
                return Response({'message': 'Transaction money is not enough'}, status=status.HTTP_403_FORBIDDEN)
            if not transaction.success:
                return Response({'message': 'Transaction was not successful'}, status=status.HTTP_403_FORBIDDEN)
            try:
                other_seat = Seat.objects.get(index=index, match=match)
            except:
                try:
                    seat = transaction.seat
                    return Response({'message': 'This transaction is used for another seat'},
                                    status=status.HTTP_403_FORBIDDEN)
                except:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveTicket(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, uid, pk):
        try:
            user = User.objects.get(pk=uid)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if user != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        seat = user.seat_set.get(pk=pk)
        serializer = SeatSerializer(seat)
        return Response(serializer.data)
