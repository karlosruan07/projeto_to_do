from django.db import models
# Create your models here.

STATUS = (
    ('doing', 'Doing'),
    ('done', 'Done'),
)

class Task(models.Model):
    title = models.CharField(max_length=255)#charfield é recomendado para trechos pequenos (titulo)
    description = models.TextField()#recomendado para textos grades
    status = models.CharField(max_length=5, #aqui irá escolher uma opção
        choices=STATUS,                    )
    created_at = models.DateTimeField(auto_now_add=True)#pega a data da criação automaticamente
    update_at = models.DateTimeField(auto_now=True)#Depois de ja ter ter a data de criação então ele só atualiza a data
    
    def __str__(self):
        return self.title
    

