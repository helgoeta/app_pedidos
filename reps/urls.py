from unicodedata import name
from django.urls import path
from .views import HomeView, ClienteListView, ClienteDetailView, PedidoDetailView, PedidoListView, addPostPedido, addPostCliente, updatePostCliente, ProdutoListView, ProdutoDetailView, addPostProduto

urlpatterns = [
    path('', HomeView, name='index'),
    path('clientes/', ClienteListView.as_view(), name='clientes'),
    path('clientes/<int:pk>/detalhes', ClienteDetailView.as_view(), name='cliente-detalhes'),
    path('clientes/cadastrar', addPostCliente.as_view(), name='cadastro-cliente'),
    path('clientes/<int:pk>/alterar', updatePostCliente.as_view(), name='altera-cliente'),
    path('produtos/', ProdutoListView.as_view(), name='produtos'),
    path('produtos/<int:pk>/detalhes', ProdutoDetailView.as_view(), name='produto-detalhes'),
    path('produtos/cadastrar', addPostProduto.as_view(), name='cadastro-produto'),
    path('pedidos', PedidoListView.as_view(), name='pedidos'),
    path('pedidos/<int:pk>/detalhes', PedidoDetailView.as_view(), name='pedido_detalhe'),
    path('pedidos/novo', addPostPedido.as_view(), name='novo-pedido')
]
