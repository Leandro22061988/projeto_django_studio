from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

def blog(request):
    blog_posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'blog_posts': blog_posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            
            # Verificar se o usuário está autenticado antes de atribuir ao autor
            if request.user.is_authenticated:
                post.author = request.user
            else:
                # Lógica adicional para lidar com usuários não autenticados, se necessário
                # Exemplo: Redirecionar para a página de login
                return redirect('login')

            post.save()
            return redirect('blog')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('blog')
