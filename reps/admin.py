from dataclasses import fields
from django.contrib import admin
from reps.models import Empresa, Cliente, Produto

# Register the Admin classes for models using the decorator
@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    pass

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'tabela_preco')
    fields = ['nome', ('codigo', 'multiplo', 'tabela_preco')]