# No arquivo contato/urls.py

from django.urls import path
from .views import ContatoListView, ContatoCreateView, ContatoUpdateView, ContatoDeleteView

urlpatterns = [
    path('', ContatoListView.as_view(), name='contato-list'),
    path('novo/', ContatoCreateView.as_view(), name='contato-create'),
    path('<int:pk>/editar/', ContatoUpdateView.as_view(), name='contato-update'),
    path('<int:pk>/excluir/', ContatoDeleteView.as_view(), name='contato-delete'),
]
