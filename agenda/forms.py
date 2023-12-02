from django import forms
from .models import Agenda

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['nome', 'email', 'telefone', 'servico', 'data', 'horario']
