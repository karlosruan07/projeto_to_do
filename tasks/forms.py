from django import forms
from .models import Task

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Form_tarefa(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description']
        

class Cadastrar_usuario(UserCreationForm):
    email = forms.EmailField(max_length=100)#registro de email obrigatorio
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def clean_email(self):
        e = self.cleaned_data['email']#pega o objeto email da lista da classe User acima
        if User.objects.filter(email=e).exists():
            raise ValidationError(f"O email {e} já existe.")

        return e

