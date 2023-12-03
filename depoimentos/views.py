# No arquivo views.py do app depoimentos

from django.shortcuts import render, get_object_or_404, redirect
from .models import Depoimento
from .forms import DepoimentoForm

def depoimentos(request):
    depoimentos = Depoimento.objects.all()
    return render(request, 'depoimentos/depoimentos_list.html', {'depoimentos': depoimentos})

def criar_depoimento(request):
    if request.method == 'POST':
        form = DepoimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('depoimentos:depoimentos-list')
    else:
        form = DepoimentoForm()
    return render(request, 'depoimentos/depoimento_form.html', {'form': form})

def atualizar_depoimento(request, pk):
    depoimento = get_object_or_404(Depoimento, pk=pk)
    if request.method == 'POST':
        form = DepoimentoForm(request.POST, instance=depoimento)
        if form.is_valid():
            form.save()
            return redirect('depoimentos:depoimentos-list')
    else:
        form = DepoimentoForm(instance=depoimento)
    return render(request, 'depoimentos/depoimento_form.html', {'form': form})

def excluir_depoimento(request, pk):
    depoimento = get_object_or_404(Depoimento, pk=pk)
    depoimento.delete()
    return redirect('depoimentos:depoimentos-list')
