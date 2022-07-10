from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from tutorials.models import AvaliacaoTutorial
from users.forms import UserForm
from aplicacao.forms import AplicacaoTutorialForm
from aplicacao.models import AplicacaoTutorial
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# AvaliacaoTutorial, AplicacaoTutorial


#view para cadastrar usuários
@login_required
def create_aplicacao(request):
    if request.user.is_staff:
            
        if request.method == "POST":
            form = AplicacaoTutorialForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/")
            else:
                context ={  
                    'form': form
                }
                
                return render(request, "aplicacao/form.html", context)
        else:
            form = AplicacaoTutorialForm()
            context ={
                    'form': form
                }
                
            return render(request, "aplicacao/form.html", context)
    else:
        return HttpResponse('Você não possui permissão de ADMIN')
    

#view para cadastrar usuários
@login_required
def excluir_aplicacao(request, aplicacao_id):
    if request.user.is_staff:
        AplicacaoTutorial.objects.get(pk=aplicacao_id).delete()
        
        return HttpResponseRedirect("/users")  
    else:
        return HttpResponse('Você não possui permissão de ADMIN')
 

@login_required
def aplicacao_edit(request, aplicacao_id):
    if request.user.is_staff:
        aplicacao = AplicacaoTutorial.objects.get(pk=aplicacao_id)

        if request.method == "POST":
            form = AplicacaoTutorialForm(request.POST, instance=aplicacao)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/users")
        else:
            form = AplicacaoTutorialForm(instance=aplicacao)
        
        context ={
            'form': form,
            'users': aplicacao.id
        }
        
        return render(request, "aplicacao/form.html", context)
    else:
        return HttpResponse('Você não possui permissão de ADMIN')