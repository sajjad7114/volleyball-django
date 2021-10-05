from rest_framework.views import APIView
from .serializers import UserSerializers
from rest_framework.response import Response
from rest_framework import status


class UserViewSets(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)

        if serializer.is_valid():
            token = serializer.save()

            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
