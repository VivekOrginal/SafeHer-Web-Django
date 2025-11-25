from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone = models.CharField(max_length=15)
    emergency_contact1 = models.CharField(max_length=15, blank=True)
    emergency_contact2 = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)
    is_police = models.BooleanField(default=False)
    
class PoliceStation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    
    def __str__(self):
        return self.name