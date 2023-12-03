from django.shortcuts import render, get_object_or_404, redirect
from .models import Agenda
from .forms import AgendaForm  # Certifique-se de criar um formulário para o modelo Agenda
from .models import Servico  # Certifique-se de importar o modelo Servico

def agenda(request):
    horarios_disponiveis = ["08:00", "09:00", "10:00"]  # Substitua pelos horários reais
    agendamentos = Agenda.objects.all()  # Modifique para obter os agendamentos reais do banco de dados

    return render(request, 'agenda/agenda.html', {'horarios_disponiveis': horarios_disponiveis, 'agendamentos': agendamentos})

def agendamento_add(request, horario):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            agendamento = form.save(commit=False)
            agendamento.horario = horario
            agendamento.save()
            return redirect('agenda:agenda')
    else:
        form = AgendaForm()

    return render(request, 'agenda/agendamento_add.html', {'form': form, 'horario': horario})

def agendamento_edit(request, agendamento_id):
    agendamento = get_object_or_404(Agenda, id=agendamento_id)

    if request.method == 'POST':
        form = AgendaForm(request.POST, instance=agendamento)
        if form.is_valid():
            form.save()
            return redirect('agenda:agenda')
    else:
        form = AgendaForm(instance=agendamento)

    return render(request, 'agenda/agendamento_edit.html', {'form': form, 'agendamento_id': agendamento_id})

def agendamento_cancelar(request, agendamento_id):
    agendamento = get_object_or_404(Agenda, id=agendamento_id)

    if request.method == 'POST':
        agendamento.delete()
        return redirect('agenda:agenda')

    return render(request, 'agenda/agendamento_cancelar.html', {'agendamento': agendamento})

def ver_horarios(request):
    if request.method == 'POST':
        # Processar o formulário, obter o serviço selecionado e buscar os horários disponíveis
        servico_id = request.POST.get('servico')  # Certifique-se de ter um campo 'servico' no seu formulário
        servico = get_object_or_404(Servico, id=servico_id)
        horarios_disponiveis = servico.horarios_disponiveis.all()  # Modifique conforme a relação entre Servico e Horario

        # Renderizar a página com os horários disponíveis
        return render(request, 'agenda/ver_horarios.html', {'horarios_disponiveis': horarios_disponiveis})

    # Se o método não for POST, você pode renderizar a página inicial ou redirecionar para a home
    return render(request, 'agenda/home.html')  # Certifique-se de ter um arquivo home.html no seu diretório templates
