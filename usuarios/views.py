from django.shortcuts import redirect, render
from django.contrib.auth.models import User


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
    return render(request, 'usuarios/login.html')


def dashboard(request):
    pass


def logout(request):
    pass
