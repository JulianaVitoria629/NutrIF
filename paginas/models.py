'''
from django.db import models

class Base(models.Model):
    cadastroprod = models.DateField("Data de cadastro de produto", auto_now_add=True)
    abastecimento = models.DateField("Data de abastecimento do estoque", auto_now= True)

class Alimento(Base):
    nomeAlimento = models.CharField("Nome", max_length= 50 )
    unidadeDeMedida = models.CharField("Unidade de Medida", max_length= 10)
    codigoDacategoria = models.CharField("Codigo da categoria do Alimento", max_length= 45)

class Categoria(models):
    nome = models.CharField("Nome", max_length= 20)
    Descricao = models.CharField("Descrição", max_length= 200)
    codigo = models.CharField("Código", max_length= 5)
    '''