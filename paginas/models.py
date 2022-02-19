'''
from django.db import models
from django.db.models import base

class Base(models.Model):
    cadastroprod = models.DateField("Data de cadastro de produto", auto_now_add=True)
    abastecimento = models.DateField("Data de abastecimento do estoque", auto_now= True)
    ativo = models.BooleanField("Ativo?" default= True)

class Alimento(Base):
    nomeAlimento = models.CharField("Nome", max_length= 50 )
    unidadeDeMedida = models.CharField("Unidade de Medida", max_length= 10)
    codigoDacategoria = models.CharField("Codigo da categoria do Alimento", max_length= 45)

class Categoria(Base):
    nome = models.CharField("Nome", max_length= 20)
    Descricao = models.CharField("Descrição", max_length= 200)
    codigo = models.CharField("Código", max_length= 5)

class Fornecedor(Base):
    nome = models.CharField("Nome do fornecedor", max_length= 50)
    Endereco = models.CharField("Endereço", max_length=100)
    cnpj= models.CharField("CNPJ", max_length=14)

class Funcionario(models):
    nome = models.CharField("Nome do Funcionario", max_length = 60)
    telefone = models.CharField("Telefone" max_length= 11)
    senha = models.CharField("Senha", max_length= 256)
    tipo = models.CharField("Tipo", max_length= 15)
    matricula = models.CharField("Matrícula", max_length= 9)

class Validade(models):
    nomeAlimento = models.CharField("Nome do alimento", max_length= 50)
    dataValidade = models.DateField("Data", auto_now= True)
    quantidade = models.IntegerField("Quantidade", max_length= 10)
'''