
from django.urls import path
from . import views

urlpatterns = [
    
    path('hello_word', views.hello_word, name='hello_word'),
]
