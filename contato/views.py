# No arquivo contato/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Contato
from .forms import ContatoForm

class ContatoListView(ListView):
    model = Contato
    template_name = 'contato/contato_list.html'
    context_object_name = 'contatos'

class ContatoCreateView(CreateView):
    model = Contato
    form_class = ContatoForm
    template_name = 'contato/contato_form.html'
    success_url = reverse_lazy('contato-list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Contato criado com sucesso!')
        return response

class ContatoUpdateView(UpdateView):
    model = Contato
    form_class = ContatoForm
    template_name = 'contato/contato_form.html'
    success_url = reverse_lazy('contato-list')

class ContatoDeleteView(DeleteView):
    model = Contato
    template_name = 'contato/contato_confirm_delete.html'
    success_url = reverse_lazy('contato-list')
