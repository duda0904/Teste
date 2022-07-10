from django.db import models

# Create your models here.
class AplicacaoTutorial(models.Model):
    nome = models.CharField(max_length=100)
    funcionalidade = models.CharField(max_length=255)

    def __str__(self):
        return self.nome