from django.db import models

from django.contrib.auth.models import User

class Glucose(models.Model):
    device = models.CharField(name='device', max_length=120)
    serie = models.CharField(name='serie', max_length=120)
    timestamp = models.DateTimeField(name='timestamp', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
