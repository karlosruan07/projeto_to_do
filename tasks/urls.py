
from django.urls import path
from . import views
from .views import lista_tarefas, seunome, login, semantico, detalhe_tarefa
urlpatterns = [
    #####  URLs de estudos   ####
    path('hello_word', views.hello_word, name='hello_word'),
    path('login/',views.login, name='login'),
    path('semantico/', views.semantico, name='semantico'),
    path('seunome/<str:seunome>/',views.seunome, name='seunome'),#passando argumentos na url

    
    #####  URLs TASKS  #######
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('detalhe_tarefa/<int:pk>/', views.detalhe_tarefa, name='detalhe_tarefa'),
    
]
