from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirecione para a página desejada após o login bem-sucedido
            messages.success(request, 'Login realizado com sucesso!')
            return redirect('home.html')
        else:
            # Usuário ou senha incorretos
            messages.error(request, 'Usuário ou senha incorretos. Tente novamente ou entre em contato com o administrador.')

    return render(request, 'login/login.html')
