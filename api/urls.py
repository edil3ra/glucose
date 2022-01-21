from django.urls import path
from .views import ListGlucose, DetailGlucose

urlpatterns = [
    path('glucoses/<int:pk>/', DetailGlucose.as_view()),
    path('glucoses/', ListGlucose.as_view()),
]
