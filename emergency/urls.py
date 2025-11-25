from django.urls import path
from . import views

urlpatterns = [
    path('trigger-sos/', views.trigger_sos, name='trigger_sos'),
    path('update-location/', views.update_location, name='update_location'),
]