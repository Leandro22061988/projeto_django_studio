# usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CadastroForm

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Salvar o número de telefone no modelo
            user.telefone = form.cleaned_data['telefone']
            user.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')
        else:
            messages.error(request, 'Corrija os erros abaixo.')
    else:
        form = CadastroForm()

    return render(request, 'usuarios/cadastro.html', {'form': form})
