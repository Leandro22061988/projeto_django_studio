# No arquivo contato/forms.py

from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone', 'endereco']

    def __init__(self, *args, **kwargs):
        super(ContatoForm, self).__init__(*args, **kwargs)
        # Adicione atributos personalizados, se necessário
        self.fields['nome'].widget.attrs['placeholder'] = 'Digite o nome'
        self.fields['email'].widget.attrs['placeholder'] = 'Digite o e-mail'
        self.fields['telefone'].widget.attrs['placeholder'] = 'Digite o telefone'
        self.fields['endereco'].widget.attrs['placeholder'] = 'Digite o endereço'
