
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import Cadastrar_usuario

import datetime

#####  bibliotecas DO TASKS #####
from .models import Task
from .forms import Form_tarefa


###### VIEWs de estudo  ######
def hello_word(request):
    return HttpResponse('<h1> Olá, Mundo ! </>')


# a função pela o argumento e usa como parâmetro.
def seunome(request, seunome):
    return render(request, 'arquivos_html/seunome.html', {'seunome': seunome})


#####  FUNÇÕES DO TASKS #####
@login_required
def lista_tarefas(request):
    
    if request.user.is_authenticated:
    
        search = request.GET.get('search')
        
        tarefas_concluidas_recente = tasks = Task.objects.filter(status='done', update_at__gt=datetime.datetime.now() - datetime.timedelta(days=30), user=request.user).count()
        tarefas_concluidas = Task.objects.filter(status='done', user=request.user).count()
        tarefas_incom = Task.objects.filter(status='doing', user=request.user).count()
                
        if search:
            todas_tarefas = Task.objects.filter(title__icontains=search, user=request.user)#para buscar por outro atributo então é só mudar o title que está passado como parâmetro
            
        else:
        
            tasks_list = Task.objects.filter(user=request.user)
            paginacao = Paginator(tasks_list, 3)    
            page = request.GET.get('page')
            tasks = paginacao.get_page(page)
            contexto = {"tasks_list": tasks_list, "tarefas_concluidas_recente":tarefas_concluidas_recente,
            "tarefas_concluidas":tarefas_concluidas, "tarefas_incom":tarefas_incom}
        return render(request, 'arquivos_html/tasks/lista_tarefas.html', contexto )
    else:
        return redirect('login')

@login_required
def detalhe_tarefa(request, pk):
     
    
    tarefa = get_object_or_404(Task, id=pk, user=request.user)
    return render(request, 'arquivos_html/tasks/detalhe_tarefa.html', {"tarefa": tarefa})


@login_required
def adicionar_tarefa(request):
    if request.method == 'POST':
        form = Form_tarefa(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.status = 'done'
            post.user = request.user
            post.save()
            return redirect('lista_tarefas')
        
    else:
        form = Form_tarefa()
        
    return render(request, 'arquivos_html/tasks/adicionar_tarefa.html', {"form": form})


@login_required
def editar_tarefa(request, id):
    
    tarefa_obtida = get_object_or_404(Task, pk=id, user=request.user)#busca o id de uma task de user authenticado
    
    form = Form_tarefa(instance=tarefa_obtida)
    if (request.method == 'POST'):
        form = Form_tarefa(request.POST,instance=tarefa_obtida)
        if(form.is_valid()):
            form.save()
            return redirect('lista_tarefas')
        else:
            return render(request, 'arquivos_html/tasks/editar_tarefa.html', {"form":form})
    return render(request, 'arquivos_html/tasks/editar_tarefa.html', {"form":form, "tarefa_obtida":tarefa_obtida})

@login_required
def confirmar_delete_tarefa(request, id):
    id_tarefa = get_object_or_404(Task, pk=id, user=request.user)
    return render(request, 'arquivos_html/tasks/confirmar_delete_tarefa.html', {"id":id_tarefa.id})


@login_required
def deletar_tarefa(request, id):
    tarefa_obtida = get_object_or_404(Task, pk=id, user=request.user)
    tarefa_obtida.delete()
    messages.info(request, 'Item apagado com sucesso !')
    return redirect('lista_tarefas')


def mudar_status(request, id):
    tarefa_obtida = get_object_or_404(Task, pk=id, user=request.user)
    
    if tarefa_obtida.status == 'done':
        tarefa_obtida.status = 'doing'
    else:
        tarefa_obtida.status = 'done'
    tarefa_obtida.save()
    return redirect('lista_tarefas')


def filtro_status(request, status):
    tasks = Task.objects.filter(status__icontains=status, user=request.user)    
    return render(request, 'arquivos_html/tasks/listas.html', {"tasks": tasks})


class Criar_usuario(CreateView):
    template_name = 'registration/registro.html'
    form_class = Cadastrar_usuario
    success_url = reverse_lazy('lista_tarefas')
    
    




