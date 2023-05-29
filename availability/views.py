from rest_framework import viewsets
from database.models import Time_Av
from .serializers import AvailabilitySerializer

class AvailabilityViewSet(viewsets.ModelViewSet):
    queryset = Time_Av.objects.all()
    serializer_class = AvailabilitySerializer
