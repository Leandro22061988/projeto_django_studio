# usuarios/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CadastroForm(UserCreationForm):
    telefone = forms.CharField(max_length=20, required=True, help_text='Informe seu número de telefone')

    class Meta:
        model = CustomUser
        fields = ['nome', 'sobrenome', 'telefone', 'email', 'password1', 'password2']
