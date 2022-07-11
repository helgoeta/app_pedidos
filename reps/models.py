from audioop import reverse
from django.db import models
from django.urls import reverse

class Empresa(models.Model):
    """Modelo que representa a Empresa"""
    nome=models.CharField(max_length=200)
    nome_responsavel=models.CharField(max_length=200)
    email=models.EmailField
    data_cricao=models.DateField(auto_now_add=True)
    ultima_alteracao=models.DateTimeField(auto_now=True)

    def __str__(self):
        """String que representa o Model object"""
        return self.nome

class Cliente(models.Model):
    """Modelo que representa o terceiro"""
    razao_social=models.CharField(max_length=200, verbose_name='Razão Social')
    data_de_cadastro=models.DateTimeField(auto_now_add=True)
    ultima_alteracao=models.DateTimeField(auto_now=True)
    empresa_id=Empresa(id)

    def __str__(self):
        return self.razao_social

    class Meta:
        ordering = ['razao_social']

    def get_absolute_url(self):
        return reverse('clientes')

class Produto(models.Model):
    """Model que representa os produtos"""
    nome=models.CharField(max_length=200)
    codigo=models.CharField(max_length=120)
    tabela_preco=models.DecimalField(max_digits=20, decimal_places=2)
    multiplo=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    ultima_alteracao=models.DateTimeField(auto_now=True)
    empresa_id=Empresa(id)
    
    def __str__(self):
        return self.nome

    
    class Meta:
        ordering = ['nome']

    def get_absolute_url(self):
        return reverse('produtos')


class Pedido(models.Model):
    cliente_id=models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True)
    razao_social=models.CharField(max_length=200, verbose_name='Razão Social')
    total=models.DecimalField(max_digits=20,decimal_places=2)
    data_criacao=models.DateTimeField(auto_now=True)
    data_emissao=models.DateTimeField(auto_now=True)
    info_adicionais=models.CharField(max_length=500)
    condicao_pagmento=models.CharField(max_length=120)
    ultima_alteracao=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.razao_social

    class Meta:
        ordering = ['razao_social']