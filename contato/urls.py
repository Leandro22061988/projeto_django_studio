# contato/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import ContatoListView, ContatoCreateView, ContatoUpdateView, ContatoDeleteView

urlpatterns = [
    path('', ContatoListView.as_view(), name='contato-list'),
    path('novo/', ContatoCreateView.as_view(), name='contato-create'),
    path('<int:pk>/editar/', ContatoUpdateView.as_view(), name='contato-update'),
    path('<int:pk>/excluir/', ContatoDeleteView.as_view(), name='contato-delete'),
]

# Adicione o seguinte ao final para servir arquivos estáticos durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
