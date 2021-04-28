from django import forms
from .models import Task

class Form_tarefa(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description']
        

