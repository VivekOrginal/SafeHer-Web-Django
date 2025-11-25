from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SOSAlert, LiveTracking
import json

@api_view(['POST'])
def trigger_sos(request):
    try:
        latitude = float(request.data.get('latitude'))
        longitude = float(request.data.get('longitude'))
        
        # Create anonymous user if not logged in
        if request.user.is_anonymous:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            user, created = User.objects.get_or_create(
                username='anonymous_sos',
                defaults={'email': 'sos@example.com'}
            )
        else:
            user = request.user
        
        # Create SOS alert
        sos = SOSAlert.objects.create(
            user=user,
            latitude=latitude,
            longitude=longitude
        )
        
        # Send emergency alerts
        send_emergency_alerts(sos)
        
        return Response({
            'success': True,
            'sos_id': sos.id,
            'tracking_url': f'/track/{sos.id}/'
        })
        
    except Exception as e:
        return Response({'error': str(e)})

@api_view(['POST'])
def update_location(request):
    try:
        sos_id = request.data.get('sos_id')
        latitude = float(request.data.get('latitude'))
        longitude = float(request.data.get('longitude'))
        
        sos = SOSAlert.objects.get(id=sos_id)
        
        # Update live tracking
        LiveTracking.objects.create(
            sos_alert=sos,
            latitude=latitude,
            longitude=longitude
        )
        
        return Response({'success': True})
        
    except Exception as e:
        return Response({'error': str(e)})

def send_emergency_alerts(sos):
    # Send SMS to emergency contacts
    # Send notification to police
    pass

def sos_page(request):
    return render(request, 'emergency/sos.html')

def track_location(request, sos_id):
    try:
        sos = SOSAlert.objects.get(id=sos_id)
        tracking_data = LiveTracking.objects.filter(sos_alert=sos).order_by('-timestamp')
        return render(request, 'emergency/track.html', {
            'sos': sos,
            'tracking_data': tracking_data
        })
    except SOSAlert.DoesNotExist:
        return render(request, 'emergency/not_found.html')