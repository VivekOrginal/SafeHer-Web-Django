from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from reports.views import report_incident
from emergency.views import sos_page, track_location
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')

def safety_view(request):
    return render(request, 'safety/safety_map.html')

def guide_view(request):
    return render(request, 'guide.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('report/', report_incident, name='report'),
    path('sos/', sos_page, name='sos'),
    path('safety/', safety_view, name='safety'),
    path('guide/', guide_view, name='guide'),
    path('track/<int:sos_id>/', track_location, name='track'),
    path('api/', include('reports.urls')),
    path('api/', include('emergency.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)