
from django.urls import path
from . import views
from .views import lista_tarefas, seunome, detalhe_tarefa, adicionar_tarefa

urlpatterns = [
    #####  URLs de estudos   ####
    path('hello_word', views.hello_word, name='hello_word'),
    path('seunome/<str:seunome>/',views.seunome, name='seunome'),#passando argumentos na url

    
    #####  URLs TASKS  #######
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('detalhe_tarefa/<int:pk>/', views.detalhe_tarefa, name='detalhe_tarefa'),
    path('adicionar_tarefa/', views.adicionar_tarefa, name='adicionar_tarefa'),
    path('editar_tarefa/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('confirmar_delete_tarefa/<int:id>/', views.confirmar_delete_tarefa, name='confirmar_delete_tarefa'),
    path('deletar_tarefa/<int:id>/', views.deletar_tarefa, name='deletar_tarefa'),
    
    
    #####  URLs de cadastro e login  #######
    path('cadastrar/', views.Criar_usuario.as_view(), name='cadastrar'),
]
