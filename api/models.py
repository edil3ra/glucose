from django.db import models
from django.contrib.auth.models import User

class Glucose(models.Model):
    name = models.CharField(name='name', max_length=120)
    text = models.TextField(name='text')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
