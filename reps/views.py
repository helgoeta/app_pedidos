from django.shortcuts import render
from reps.models import Cliente, Produto

def index(request):
    """View function for home page of site"""
    num_clientes = Cliente.objects.count()
    num_produtos = Produto.objects.count()

    context = {
        'num_clientes': num_clientes,
        'num_produtos': num_produtos,
    }

    return render(request, 'index.html', context=context)