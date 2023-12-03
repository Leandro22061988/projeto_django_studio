from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from home.views import home  
from blog.views import blog
from agenda.views import agenda
from login.views import login
from sobre.views import sobre
from depoimentos.views import depoimentos
from contato.views import ContatoListView 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('blog/', include('blog.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('agenda/', include('agenda.urls')),
    path('login/', include('login.urls')),
    path('sobre/', include('sobre.urls')),
    path('depoimentos/', include('depoimentos.urls')),  # Adicionado a barra no final
    path('contato/', ContatoListView.as_view(), name='contato-list'),  
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)