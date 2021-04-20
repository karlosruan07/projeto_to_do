
from django.urls import path
from . import views
from .views import lista_tarefas, seunome
urlpatterns = [
    
    path('hello_word', views.hello_word, name='hello_word'),
    
    #####  URLs TASKS  #######
    path('', views.lista_tarefas, name='lista_tarefas'),
    path('seunome/<str:seunome>/',views.seunome, name='seunome'),#passando argumentos na url
]
