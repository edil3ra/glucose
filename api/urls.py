from django.urls import path
from .views import ListGlucose, DetailGlucose, ListGlucoseByUser, DetailGlucoseByUser

urlpatterns = [
    path('v1/levels/<int:pk>/', DetailGlucose.as_view()),
    path('v1/levels/', ListGlucose.as_view()),
    path('v1/levels/user/<int:pk>/', ListGlucoseByUser.as_view()),
    path('v1/levels/<int:pk>/user/<int:pk_user>/', DetailGlucoseByUser.as_view()),
]
