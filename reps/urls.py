from unicodedata import name
from django.urls import path
from .views import HomeView, ClienteListView, ClienteDetailView, addPostCliente, ProdutoListView, ProdutoDetailView, addPostProduto

urlpatterns = [
    path('', HomeView, name='index'),
    path('clientes/', ClienteListView.as_view(), name='clientes'),
    path('clientes/<int:pk>/detalhes', ClienteDetailView.as_view(), name='cliente-detalhes'),
    path('clientes/cadastrar', addPostCliente.as_view(), name='cadastro-cliente'),
    path('produtos/', ProdutoListView.as_view(), name='produtos'),
    path('produtos/<int:pk>/detalhes', ProdutoDetailView.as_view(), name='produto-detalhes'),
    path('produtos/cadastrar', addPostProduto.as_view(), name='cadastro-produto')
]
