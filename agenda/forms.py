# forms.py
from django import forms
from .models import Agenda

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = '__all__'
