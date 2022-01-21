from rest_framework import generics
from .models import Glucose
from .serializers import GlucoseSerializer
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
import django_filters



class TimestampFilter(django_filters.FilterSet):
    start = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='gte')
    end = django_filters.DateTimeFilter(field_name="timestamp", lookup_expr='lte')

    class Meta:
        model = Glucose
        fields = ['start', 'end']


class ListGlucose(generics.ListCreateAPIView):
    queryset = Glucose.objects.all()
    serializer_class = GlucoseSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_class = TimestampFilter

    # filterset_fields = ['timestamp__range']



class DetailGlucose(generics.RetrieveUpdateDestroyAPIView):
    queryset = Glucose.objects.all()
    serializer_class = GlucoseSerializer


class ListGlucoseByUser(generics.ListCreateAPIView):
    serializer_class = GlucoseSerializer
    filter_class = TimestampFilter
    def get_queryset(self):
        user_id = self.kwargs['pk']
        User = get_user_model()
        user = get_object_or_404(User, pk=user_id)
        return Glucose.objects.filter(user=user)


class DetailGlucoseByUser(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GlucoseSerializer
    def get_queryset(self):
        glucose_id = self.kwargs['pk']
        user_id = self.kwargs['pk_user']
        User = get_user_model()
        get_object_or_404(User, pk=user_id)
        get_object_or_404(Glucose, pk=glucose_id)
        return Glucose.objects.filter(user__pk=user_id, pk=glucose_id)

