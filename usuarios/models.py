# usuarios/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    sobrenome = models.CharField(max_length=100, verbose_name='Sobrenome')
    telefone = models.CharField(max_length=20, verbose_name='Telefone')
    email = models.EmailField(unique=True, verbose_name='E-mail')

    # Remova 'email' de REQUIRED_FIELDS
    REQUIRED_FIELDS = ['nome', 'sobrenome', 'telefone']

    # Defina 'email' como USERNAME_FIELD
    USERNAME_FIELD = 'email'

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
