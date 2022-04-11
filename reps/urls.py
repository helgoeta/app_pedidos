from unicodedata import name
from django.urls import path
from reps import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.ClienteListView.as_view(), name='clientes'),
    path('clientes/<int:pk>/detalhes', views.ClienteDetailView.as_view(), name='cliente-detalhes'),
    path('produtos/', views.ProdutoListView.as_view(), name='produtos'),
    path('produtos/<int:pk>/detalhes', views.ProdutoDetailView.as_view(), name='produto-detalhes'),
]
