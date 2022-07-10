from django.shortcuts import render, get_object_or_404
from tutorials.models import AplicacaoTutorial, Tutorial, AvaliacaoTutorial
from tutorials.forms import AvaliacaoTutorialForm, TutorialForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.datastructures import MultiValueDictKeyError



#view para listar tutorials
def listar(request):
    try:

        params_aplicacao = request.GET['aplicacao']
        aplicacao = AplicacaoTutorial.objects.filter(nome=params_aplicacao).first()
        tutorials = Tutorial.objects.filter(aplicacao=aplicacao)
        context = {
            "tutorials": tutorials
        }
        return render(request, 'tutorials/list.html', context)
    except MultiValueDictKeyError:
        tutorials = Tutorial.objects.all()
        context = {
            "tutorials": tutorials
        }
        return render(request, 'tutorials/list.html', context)


#view para listar detalhes de tutorials
@login_required
def detail(request, tutorials_id):
    tutorials = Tutorial.objects.get(pk=tutorials_id)
    try:
        avaliacao = AvaliacaoTutorial.objects.get(post=tutorials_id)
    except AvaliacaoTutorial.DoesNotExist:
        avaliacao = None    
    

    context = {
        "tutorials": tutorials,
        "avaliacao": avaliacao,
        "avaliacao_geral": AvaliacaoTutorial.objects.all()

    }
    return render(request, 'tutorials/detail.html', context)

#view para cadastrar usuários
@login_required
def create_tutorials(request):
    if request.user.is_staff:
        if request.method == "POST":
            form = TutorialForm(request.POST, request.FILES)
            if form.is_valid():
                tutorial = form.save(commit=False)
                tutorial.user = request.user
            
                tutorial.save()
                return HttpResponseRedirect("/tutorials")
        else:
            form = TutorialForm()
        
        context = {
            'form': form
        }
        
        return render(request, "tutorials/form.html", context)
    else:
        return HttpResponse('Você precisa da permissão de ADMIN')


#view para cadastrar usuários
@login_required
def excluir(request, tutorials_id):
    if request.user.is_staff:
        tutorial = Tutorial.objects.get(pk=tutorials_id)
        if tutorial.user  or tutorial.user.is_admin:
            tutorial.delete()
            return HttpResponseRedirect("/tutorials")    
        else:
            return HttpResponse('Você não tem permissão para apagar')
    else:
        return HttpResponse('Você precisa da permissão de ADMIN')

@login_required
def tutorials_edit(request, tutorials_id):
    if request.user.is_staff:
        tutorial = get_object_or_404(Tutorial, pk=tutorials_id)
        if tutorial.user == request.user or tutorial.user.is_admin:

            if request.method == "POST":
                form = TutorialForm(request.POST, instance=tutorial)
                if form.is_valid():
                    tutorial = form.save(commit=False)
                    tutorial.user = request.user
                
                    tutorial.save()
                    return HttpResponseRedirect("/tutorials")
            else:
                form = TutorialForm(instance=tutorial)
            
            context = {
                'form': form,
                'tutorials': tutorials_id
            }
            
            return render(request, "tutorials/form.html", context)
        else:
            return HttpResponse('Você não tem permissão para apagar')

    else:
        return HttpResponse('Você precisa da permissão de ADMIN')




#view para listar detalhes de tutorials
@login_required
def detail_avaliacao(request, tutorials_id):
    #avaliacao = AvaliacaoTutorial.objects.get(pk=avaliacao_id)
    avaliacao = AvaliacaoTutorial.objects.get(post=tutorials_id)

    context = {
        "avaliacao": avaliacao
    }
    return render(request, 'avaliacao/detail.html', context)

#view para cadastrar usuários
@login_required
def create_avaliacao(request, tutorials_id):
    
    tutorial = Tutorial.objects.get(pk=tutorials_id)
    if request.method == "POST":
        form = AvaliacaoTutorialForm(request.POST, request.FILES)
        if form.is_valid():
            avaliacao = form.save(commit=False)
            avaliacao.user = request.user
            avaliacao.post = tutorial
        
            avaliacao.save()
            return HttpResponseRedirect("/tutorials")
    else:
        form = AvaliacaoTutorialForm()
    
    context ={
        'form': form
    }
    
    return render(request, "avaliacao/form.html", context)



#view para cadastrar usuários
@login_required
def excluir_avaliacao(request, tutorials_id):
    avaliacao = AvaliacaoTutorial.objects.get(post=tutorials_id)
    if request.user == avaliacao.user:
        avaliacao.delete()
        return HttpResponseRedirect("/tutorials")    
    else:
        return HttpResponse('Você não tem permissão para apagar')


    

@login_required
def avaliacao_edit(request, tutorials_id):

    avaliacao = get_object_or_404(AvaliacaoTutorial, post=tutorials_id)
    if request.user.is_staff:
        tutorial = get_object_or_404(Tutorial, pk=tutorials_id)
        if tutorial.user == request.user or tutorial.user.is_admin:
    
            if request.method == "POST":
                form = AvaliacaoTutorialForm(request.POST, instance=avaliacao)
                if form.is_valid():
                    avaliacao = form.save(commit=False)
                    avaliacao.user = request.user
                
                    avaliacao.save()
                    return HttpResponseRedirect("/tutorials")
            else:
                form = AvaliacaoTutorialForm(instance=avaliacao)
            
            context = {
                'form': form,
            }
            
            return render(request, "avaliacao/form.html", context)

        else:
            return HttpResponse('Você não tem permissão para apagar')

    else:
        return HttpResponse('Você precisa da permissão de ADMIN')