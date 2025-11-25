from django.urls import path
from . import views

urlpatterns = [
    path('upload-incident/', views.upload_incident, name='upload_incident'),
]