
from django.urls import path
from .views import sobre  

urlpatterns = [

    path('sobre/', sobre, name='sobre'),  
]
