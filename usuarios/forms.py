
from django import forms
from .models import CustomUser

class CadastroForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['nome', 'sobrenome', 'telefone', 'email'] 
