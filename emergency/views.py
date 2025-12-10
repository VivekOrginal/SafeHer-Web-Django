"""
SafeHer Emergency Views - DEMO VERSION
Developer: Vivek P S
Email: viveksubhash4@gmail.com

Backend functionality removed for protection.
Purchase full project for complete implementation.
"""

from django.shortcuts import render
from django.http import JsonResponse

def demo_purchase_required(request):
    return JsonResponse({
        'error': 'Demo Version - Backend Disabled',
        'message': 'Purchase full project for backend functionality',
        'developer': 'Vivek P S',
        'email': 'viveksubhash4@gmail.com'
    }, status=403)

def trigger_sos(request):
    return demo_purchase_required(request)

def update_location(request):
    return demo_purchase_required(request)

def sos_page(request):
    return render(request, 'emergency/sos.html')

def track_location(request, sos_id):
    return render(request, 'emergency/sos.html')