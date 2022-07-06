from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        if not nome.strip():
            print('Nome não pode ficar em branco')
            return redirect('cadastro')
        if not email.strip():
            print('E-mail não pode ficar em branco')
            return redirect('cadastro')
        if not senha.strip():
            print('Senha não pode ficar em branco')
            return redirect('cadastro')
        if not senha2.strip():
            print('Senha não pode ficar em branco')
            return redirect('cadastro')
        if not senha == senha2:
            print('As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print('Usuario já cadastrado!')
            return redirect('cadastro')
        else:
            user = User.objects.create_user(
                username=nome, email=email, password=senha)
            user.save()
            print(f'Usuario {nome} cadastrado com sucesso')
            return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['password']
        if email == "" or senha == "":
            print('email e senha não pode estar em branco.')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            # Verifica username e atribui a variavel nome
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('login OK')
                return redirect('dashboard')
    else:
        return render(request, 'usuarios/login.html')


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index')


def logout(request):
    auth.logout(request)
    return redirect('index')


def cria_receita(request):
    return render(request, 'usuarios/cria_receita.html')