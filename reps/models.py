from django.db import models

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