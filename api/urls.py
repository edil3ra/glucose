from django.urls import path
from .views import ListGlucose, DetailGlucose, DetailGlucoseByUser

urlpatterns = [
    path('v1/glucoses/user/<int:pk>', DetailGlucoseByUser.as_view()),
    path('v1/glucoses/<int:pk>/', DetailGlucose.as_view()),
    path('v1/glucoses/', ListGlucose.as_view()),
]
