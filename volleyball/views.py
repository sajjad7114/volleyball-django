from rest_framework import viewsets
from .serializers import StadiumSerializer
from .models import Stadium

# Create your views here.


class StadiumViewSet(viewsets.ModelViewSet):
    serializer_class = StadiumSerializer
    queryset = Stadium.objects.all()
