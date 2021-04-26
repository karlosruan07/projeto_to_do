
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

#####  bibliotecas DO TASKS #####
from .models import Task

###### VIEWs de estudo  ######
def hello_word(request):
    return HttpResponse('<h1> Olá, Mundo ! </>')
def login(request):
    return render(request, 'arquivos_html/login.html')
def semantico(request):
    return render(request, 'arquivos_html/sematico.html')
def seunome(request, seunome):#a função pela o argumento e usa como parâmetro.
    return render(request, 'arquivos_html/seunome.html', {'seunome': seunome})


#####  FUNÇÕES DO TASKS #####
def lista_tarefas(request):
    tasks = Task.objects.all()
    return render(request, 'arquivos_html/tasks/listas.html', {"tasks":tasks})

def detalhe_tarefa(request, pk):
    tarefa = get_object_or_404(Task, id=pk)
    return render(request, 'arquivos_html/tasks/detalhe_tarefa.html', {"tarefa":tarefa})



