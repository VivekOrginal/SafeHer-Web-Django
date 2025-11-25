from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class IncidentReport(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('investigating', 'Investigating'),
        ('resolved', 'Resolved'),
    ]
    
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='incident_videos/')
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    police_station = models.ForeignKey('users.PoliceStation', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"Report {self.id} - {self.timestamp}"