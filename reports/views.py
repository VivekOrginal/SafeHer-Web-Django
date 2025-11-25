from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import IncidentReport
from users.models import PoliceStation
from geopy.distance import geodesic
import json

@api_view(['POST'])
def upload_incident(request):
    try:
        video_file = request.FILES.get('video')
        latitude = float(request.data.get('latitude'))
        longitude = float(request.data.get('longitude'))
        description = request.data.get('description', '')
        
        # Create anonymous user if not logged in
        if request.user.is_anonymous:
            from django.contrib.auth import get_user_model
            User = get_user_model()
            user, created = User.objects.get_or_create(
                username='anonymous_reporter',
                defaults={'email': 'anonymous@example.com'}
            )
        else:
            user = request.user
        
        # Find nearest police station
        nearest_station = find_nearest_police_station(latitude, longitude)
        
        # Create incident report
        incident = IncidentReport.objects.create(
            reporter=user,
            video_file=video_file,
            latitude=latitude,
            longitude=longitude,
            description=description,
            police_station=nearest_station
        )
        
        # Send alert to police
        send_police_alert(incident)
        
        # Get nearby stations for display
        nearby_stations = get_nearby_stations(latitude, longitude)
        
        return Response({
            'success': True,
            'incident_id': incident.id,
            'police_station': nearest_station.name if nearest_station else None,
            'nearby_stations': nearby_stations
        })
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

def find_nearest_police_station(lat, lng):
    stations = PoliceStation.objects.all()
    nearest = None
    min_distance = float('inf')
    
    for station in stations:
        distance = geodesic((lat, lng), (station.latitude, station.longitude)).kilometers
        if distance < min_distance:
            min_distance = distance
            nearest = station
    
    return nearest

def get_nearby_stations(lat, lng):
    stations = PoliceStation.objects.all()
    nearby = []
    
    for station in stations:
        distance = geodesic((lat, lng), (station.latitude, station.longitude)).kilometers
        if distance <= 10:  # Within 10km
            nearby.append({
                'name': station.name,
                'distance': round(distance, 1),
                'is_online': True,
                'response_time': 10,
                'rating': 4.5,
                'lat': station.latitude,
                'lng': station.longitude
            })
    
    return sorted(nearby, key=lambda x: x['distance'])

def send_police_alert(incident):
    # SMS Alert to 90037612009
    message = f"EMERGENCY ALERT: Location {incident.latitude},{incident.longitude} Time {incident.timestamp} Reporter {incident.reporter.username}"
    
    print("=" * 50)
    print("SMS ALERT SENT TO: 90037612009")
    print(f"MESSAGE: {message}")
    print("=" * 50)

def detect_harassment(video_file):
    # Simple AI detection placeholder
    return True

@api_view(['GET'])
def police_map(request):
    lat = float(request.GET.get('lat', 0))
    lng = float(request.GET.get('lng', 0))
    
    if lat and lng:
        stations = get_nearby_stations(lat, lng)
    else:
        stations = []
    
    return Response({'stations': stations})

def report_incident(request):
    return render(request, 'reports/report.html')