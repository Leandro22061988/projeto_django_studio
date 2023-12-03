# No arquivo models.py do app depoimentos

from django.db import models

class Depoimento(models.Model):
    nome = models.CharField(max_length=100)
    mensagem = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
