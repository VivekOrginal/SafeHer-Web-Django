from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from reports.views import report_incident
from emergency.views import sos_page, track_location
from django.shortcuts import render
from .sitemaps import StaticSitemap

sitemaps = {
    'static': StaticSitemap
}

def home_view(request):
    # Always show loading page first
    return render(request, 'loading.html')

def main_home_view(request):
    return render(request, 'home.html')

def safety_view(request):
    return render(request, 'safety/safety_map.html')

def guide_view(request):
    return render(request, 'guide.html')

def nearby_help_view(request):
    return render(request, 'safety/nearby_help.html')

def loading_view(request):
    return render(request, 'loading.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('home/', main_home_view, name='main_home'),
    path('report/', report_incident, name='report'),
    path('sos/', sos_page, name='sos'),
    path('safety/', safety_view, name='safety'),
    path('guide/', guide_view, name='guide'),
    path('nearby-help/', nearby_help_view, name='nearby_help'),
    path('loading/', loading_view, name='loading'),
    path('track/<int:sos_id>/', track_location, name='track'),
    path('api/', include('reports.urls')),
    path('api/', include('emergency.urls')),
    path('robots.txt', TemplateView.as_view(
        template_name='robots.txt', content_type='text/plain')),
    path('google35d4a1f1f9e0c372.html', TemplateView.as_view(
        template_name='google35d4a1f1f9e0c372.html', content_type='text/html')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)