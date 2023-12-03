
from django.shortcuts import render, redirect
from .forms import CadastroForm

def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home.html')
    else:
        form = CadastroForm()

    return render(request, 'usuarios/cadastro.html', {'form': form})

