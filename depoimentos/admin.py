# depoimentos/admin.py

from django.contrib import admin
from .models import Depoimento

@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'mensagem', 'data_publicacao')
    search_fields = ('nome', 'mensagem')
    list_filter = ('data_publicacao',)
    date_hierarchy = 'data_publicacao'
