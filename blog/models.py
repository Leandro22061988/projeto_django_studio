
from django.db import models
from django.utils import timezone
from usuarios.models import CustomUser

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)  # Adicionando campo para imagem

    def __str__(self):
        return self.title
