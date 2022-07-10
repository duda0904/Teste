from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from users.forms import UserForm, FormLogin
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


#view para listar usuários
@login_required
def listar(request):
    if request.user.is_staff:
        users = User.objects.all()
        context = {
            "users": users
        }
        return render(request, 'users/list.html', context)
    else:
        HttpResponse('Você não tem permissão de admin')

#view para listar detalhes de users
@login_required
def detail(request):

    users = User.objects.get(pk=request.user.id)
    context = {
        "users": users
    }
    return render(request, 'users/detail.html', context)

#view para cadastrar usuários
def create_user(request):
    
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/users")
        else:
     
            context ={  
                'form': form
            }
            
            return render(request, "users/form.html", context)
    else:
        form = UserForm()
        context ={
                'form': form
            }
            
        return render(request, "users/form.html", context)
    
    

#view para cadastrar usuários
@login_required
def excluir(request):
    
    User.objects.get(pk=request.user.id).delete()
    
    return HttpResponseRedirect("/users")    

@login_required
def user_edit(request):
        pessoa = User.objects.get(pk=request.user.id)
   
        
        if request.method == "POST":
            form = UserForm(request.POST, instance=pessoa)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/users")
        else:
            form = UserForm(instance=pessoa)
        
        context ={
            'form': form,
            'users': pessoa.id
        }
        
        return render(request, "users/form.html", context)


def login_view(request):
    if request.method == "POST":
            
            user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return render(request, 'users/login.html', {'error':'Houve um erro'})
        
    else:
        return render(request, 'users/login.html', {})