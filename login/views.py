from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # Redirecione para a página desejada após o login bem-sucedido
            return redirect('pagina_protegida')
        else:
            messages.error(request, 'Credenciais inválidas. Tente novamente.')

    return render(request, 'login.html')
