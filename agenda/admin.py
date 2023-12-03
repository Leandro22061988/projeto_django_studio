# agenda/admin.py

from django.contrib import admin
from .models import Agenda

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'servico', 'data', 'horario')
    search_fields = ('nome', 'servico', 'data')
    list_filter = ('servico', 'data')
    date_hierarchy = 'data'
    time_hierarchy = 'horario'
