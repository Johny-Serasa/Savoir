from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants
from django.contrib import messages, auth


# Create your views here.
def index(request):
    return render(request, 'index.html')


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    else:
        username = request.POST.get('username')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')       
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincídem')
            return redirect('/cadastro')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request,constants.ERROR,'Já existe um usuário com o mesmo username',)
            return redirect('/cadastro')

        try:
            user = User.objects.create_user(
                username=username,
                last_name=sobrenome,
                email=email,
                first_name=username,
                password=senha,
            )
            messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso.')
            return redirect('/logar')
        except:
            messages.add_message(
                request, constants.ERROR, 'Erro interno do sistema')
            return redirect('/cadastro')
        

def logar(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(request, username=username, password=senha)
        if user:
            auth.login(request, user)
            messages.add_message(request, constants.SUCCESS, 'Logado!')
            return redirect('/')
        else:
            messages.add_message(
                request, constants.ERROR, 'Username ou senha inválidos'
            )
            return redirect('/login')
        

def planos(request):
    return render(request, 'planos.html')