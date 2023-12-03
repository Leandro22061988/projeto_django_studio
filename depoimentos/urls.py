
from django.urls import path
from .views import depoimentos, criar_depoimento, atualizar_depoimento, excluir_depoimento

app_name = 'depoimentos'

urlpatterns = [
    path('', depoimentos, name='depoimentos-list'),
    path('criar/', criar_depoimento, name='depoimento-create'),
    path('<int:pk>/editar/', atualizar_depoimento, name='depoimento-update'),
    path('<int:pk>/excluir/', excluir_depoimento, name='depoimento-delete'),
]
