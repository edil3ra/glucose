from rest_framework import generics
from .models import Glucose
from .serializers import GlucoseSerializer


class ListGlucose(generics.ListCreateAPIView):
    queryset = Glucose.objects.all()
    serializer_class = GlucoseSerializer


class DetailGlucose(generics.RetrieveUpdateDestroyAPIView):
    queryset = Glucose.objects.all()
    serializer_class = GlucoseSerializer


# TODO
class DetailGlucoseByUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = Glucose.objects.all()
    serializer_class = GlucoseSerializer

    def get_queryset(self):
        User.objects.filter(Q(invited_by=request.user.id)|Q(id = request.user.id))

