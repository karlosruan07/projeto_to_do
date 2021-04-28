
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

#####  bibliotecas DO TASKS #####
from .models import Task
from .forms import Form_tarefa

###### VIEWs de estudo  ######


def hello_word(request):
    return HttpResponse('<h1> Olá, Mundo ! </>')


def login(request):
    return render(request, 'arquivos_html/login.html')


def semantico(request):
    return render(request, 'arquivos_html/sematico.html')


# a função pela o argumento e usa como parâmetro.
def seunome(request, seunome):
    return render(request, 'arquivos_html/seunome.html', {'seunome': seunome})


#####  FUNÇÕES DO TASKS #####
def lista_tarefas(request):
    tasks = Task.objects.all()
    return render(request, 'arquivos_html/tasks/listas.html', {"tasks": tasks})


def detalhe_tarefa(request, pk):
    tarefa = get_object_or_404(Task, id=pk)
    return render(request, 'arquivos_html/tasks/detalhe_tarefa.html', {"tarefa": tarefa})


def adicionar_tarefa(request):
    if request.method == 'POST':
        form = Form_tarefa(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.status = 'done'
            post.save()
            return redirect('lista_tarefas')
        
    else:
        form = Form_tarefa()
        
    return render(request, 'arquivos_html/tasks/adicionar_tarefa.html', {"form": form})


def editar_tarefa(request, id):
    tarefa_obtida = get_object_or_404(Task, pk=id)
    form = Form_tarefa(instance=tarefa_obtida)
    
    if (request.method == 'POST'):
        form = Form_tarefa(request.POST,instance=tarefa_obtida)
        if(form.is_valid()):
            form.save()
            return redirect('lista_tarefas')
        else:
            return render(request, 'arquivos_html/tasks/editar_tarefa.html', {"form":form})
    return render(request, 'arquivos_html/tasks/editar_tarefa.html', {"form":form, "tarefa_obtida":tarefa_obtida})


