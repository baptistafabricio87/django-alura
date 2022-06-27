from django.shortcuts import render

# Create your views here.
def index(request):
    receitas = {
        1:'Lasanha',
        2:'Sorvete',
        3:'Sopa de Legumes',
        4:'Caldo Verde',
        5:'Bolo de Chocolate',
        6:'Bolo de Cenoura'
    }

    dados = {
        'nomes_receitas' : receitas
    }
    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')

