from django.db import models
from django.db.models import base

class Base(models.Model):
    cadastroprod = models.DateField("Data de cadastro de produto", auto_now_add=True)
    abastecimento = models.DateField("Data de abastecimento do estoque", auto_now= True)
    ativo = models.BooleanField("Ativo?", default= True)

class Alimento(models.Model):
    nomeAlimento = models.CharField("Nome", max_length= 50 )
    unidadeDeMedida = models.CharField("Unidade de Medida", max_length= 10)
    codigoDacategoria = models.CharField("Codigo da categoria do Alimento", max_length= 45)

    def __str__(self):
        return self.nomeAlimento

class Categoria(models.Model):
    nome = models.CharField("Nome", max_length= 20)
    descricao = models.CharField("Descricao do produto", max_length= 200)
    codigo = models.CharField("Código", max_length= 5)

    def __str__(self):
        return self.descricao

class Fornecedor(models.Model):
    nome = models.CharField("Nome do fornecedor", max_length= 50)
    endereco = models.CharField("Endereco do fornecedor", max_length=100)
    cnpj= models.CharField("CNPJ", max_length=14)

class Funcionario(models.Model):
    nomeFuncionario = models.CharField("Nome do Funcionario", max_length = 60)
    telefone = models.CharField("Telefone", max_length= 11)
    senha = models.CharField("Senha", max_length= 256)
    tipo = models.CharField("Tipo", max_length= 15)
    matricula = models.CharField("Matrícula", max_length= 9)

    def __str__(self):
        return self.nomeFuncionario

class ValidadedeAlimento(models.Model):
    nomeAlimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    dataValidade = models.DateField("Data")
    quantidade = models.FloatField("Quantidade recebida")
    quantidade = models.FloatField("Quantidade recebida")
 

class Fornece(models.Model):
    nomeAlimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    cnpjFornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)

class Recebe(models.Model):
    nomeAlimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    quantidade = models.FloatField("Quantidade recebida")
    data = models.DateField("Data de recebimento")
    matriculaFuncionario= models.ForeignKey(Funcionario, on_delete=models.CASCADE)

class Utiliza(models.Model):
    nomeAlimento = models.ForeignKey(Alimento, on_delete=models.CASCADE)
    turno = models.CharField("Turno utilizou", max_length= 15)
    data = models.DateField("Data que o alimento foi utilizado")
    quantidade = models.FloatField("Quantidade utilizada")
    matriculaFuncionario= models.ForeignKey(Funcionario, on_delete=models.CASCADE)

class TelefoneFornecedor(models.Model):
    cnpjFornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    telefone = models.CharField("Telefone", max_length= 11)