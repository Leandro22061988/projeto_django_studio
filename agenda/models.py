# models.py
from django.db import models

class Servico(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Agenda(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data = models.DateField()
    horario = models.TimeField()

    def __str__(self):
        return f'{self.nome} - {self.servico} - {self.data} {self.horario}'
