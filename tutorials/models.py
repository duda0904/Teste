from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField 
from aplicacao.models import AplicacaoTutorial





class Tutorial(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = RichTextUploadingField()
    data_criacao = models.DateField(auto_now_add=True)
    data_edicao = models.DateField(auto_now=True)
    aplicacao = models.ForeignKey(AplicacaoTutorial, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class AvaliacaoTutorial(models.Model):
 
    data_criacao = models.DateTimeField(auto_now_add=True)
    avaliacao = models.IntegerField(verbose_name="Avaliação") 
    text = models.CharField(max_length=40, verbose_name="Descrição da avaliação")
    post = models.OneToOneField(Tutorial, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.avaliacao
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)
 