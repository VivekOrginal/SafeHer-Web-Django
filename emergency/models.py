from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class SOSAlert(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    audio_file = models.FileField(upload_to='sos_audio/', blank=True)
    
    def __str__(self):
        return f"SOS Alert {self.id} - {self.user.username}"

class LiveTracking(models.Model):
    sos_alert = models.ForeignKey(SOSAlert, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)