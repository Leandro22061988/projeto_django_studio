# agenda/urls.py
from django.urls import path
from .views import agenda, agendamento_add, agendamento_edit, agendamento_cancelar, ver_horarios

app_name = 'agenda'

urlpatterns = [
    path('', agenda, name='agenda'),
    path('<str:horario>/adicionar/', agendamento_add, name='agendamento_add'),
    path('<int:agendamento_id>/editar/', agendamento_edit, name='agendamento_edit'),
    path('<int:agendamento_id>/cancelar/', agendamento_cancelar, name='agendamento_cancelar'),
    path('ver_horarios/', ver_horarios, name='ver_horarios'),  # Adicione esta linha
]
