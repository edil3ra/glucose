from rest_framework import generics
from .models import Glucose
from .serializers import GlucoseSerializer


class ListGlucose(generics.ListCreateAPIView):
    queryset = Glucose.objects.all()
    serializer_class = GlucoseSerializer


class DetailGlucose(generics.RetrieveUpdateDestroyAPIView):
    queryset = Glucose.objects.all()
    serializer_class = GlucoseSerializer

