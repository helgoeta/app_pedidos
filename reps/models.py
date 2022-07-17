from audioop import reverse
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.db import models
from django.core.exceptions import ValidationError
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
    tabela_preco=models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    multiplo=models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    ultima_alteracao=models.DateTimeField(auto_now=True)
    empresa_id=Empresa(id)
    
    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('produtos')

    class Meta:
        ordering = ['nome']
        

class Pedido(models.Model):
    cliente_id=models.ForeignKey('Cliente', on_delete=models.SET_NULL, null=True, verbose_name='Razão Social')
#    numero=models.PositiveIntegerField(auto_created=True)
    total=models.DecimalField(max_digits=20,decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    data_criacao=models.DateTimeField(auto_now=True)
    data_emissao=models.DateTimeField(auto_now=True)
    info_adicionais=models.CharField(max_length=500, blank=True, null=True)
    condicao_pagmento=models.CharField(max_length=120)
    ultima_alteracao=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.razao_social
   
    def get_absolute_url(self):
        return reverse('pedidos')
