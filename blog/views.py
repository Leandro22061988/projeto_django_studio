from django.shortcuts import render
from .models import Post  # Importe o modelo Post
from blog.models import Post

def blog(request):
    # Obtenha todas as postagens do blog
    blog_posts = Post.objects.all()

    # Passe as postagens para o contexto
    return render(request, 'blog/blog.html', {'blog_posts': blog_posts})
