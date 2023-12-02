from django.urls import path
from .views import agenda

app_name = 'agenda'

urlpatterns = [
   
    path('agenda/', agenda, name='agenda'),
]
