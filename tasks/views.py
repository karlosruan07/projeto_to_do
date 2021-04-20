
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello_word(request):
    return HttpResponse('<h1> Olá, Mundo ! </>')

#####  FUNÇÕES DO TASKS #####
def lista_tarefas(request):
    return render(request, 'arquivos_html/listas.html')

def seunome(request, seunome):#a função pela o argumento e usa como parâmetro.
    return render(request, 'arquivos_html/seunome.html', {'seunome': seunome})



