# No arquivo models.py do seu aplicativo 'blog'
from django.db import models
from django.utils import timezone
from usuarios.models import CustomUser  # Importe o seu modelo de usuário personalizado

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Use o seu modelo personalizado

    def __str__(self):
        return self.title
