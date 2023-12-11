
from django.urls import path
from .views import home, LoginPageView, logout_view

urlpatterns = [
    path('home/', home, name='home'),
    path('login/', LoginPageView.as_view(), name='login'),  
    path('logout/', logout_view, name='logout'),
    
]
