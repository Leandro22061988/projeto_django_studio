from django.shortcuts import render, redirect
from .models import Agenda
from .forms import AgendaForm

def agenda(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  
    else:
        form = AgendaForm()

    return render(request, 'agenda.html', {'form': form})
