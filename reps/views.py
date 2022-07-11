from re import template
from django.shortcuts import render
from reps.models import Cliente, Produto
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.backends import BaseBackend


def HomeView(request):
    """View function for home page of site"""
    num_clientes = Cliente.objects.count()
    num_produtos = Produto.objects.count()

    context = {
        'num_clientes': num_clientes,
        'num_produtos': num_produtos,
    }

    return render(request, 'index.html', context=context)


class ClienteListView(ListView):
    model = Cliente
    paginate_by = 10
    context_object_name = 'clientes_lista'
    template_name = 'clientes/clientes_lista.html'


class ClienteDetailView(DetailView):
    model = Cliente
    context_object_name = 'cliente_detalhes'
    template_name = 'clientes/cliente_detalhes.html'


class ProdutoListView(ListView):
    model = Produto
    paginate_by = 10
    context_object_name = 'produtos_lista'
    template_name = 'produtos/produtos_lista.html'


class ProdutoDetailView(DetailView):
    model = Produto
    context_object_name = 'produto_detalhes'
    template_name = 'produtos/produto_detalhes.html'

class addPostProduto(CreateView):
    model = Produto
    template_name = 'produtos/add_produto.html'
    fields = '__all__'
