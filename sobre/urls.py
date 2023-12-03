
from django.urls import path
from .views import sobre  

urlpatterns = [

    path('', sobre, name='sobre'),  
]
