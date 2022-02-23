# Generated by Django 4.0.1 on 2022-02-23 22:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeAlimento', models.CharField(max_length=50, verbose_name='Nome')),
                ('unidadeDeMedida', models.CharField(max_length=10, verbose_name='Unidade de Medida')),
                ('codigoDacategoria', models.CharField(max_length=45, verbose_name='Codigo da categoria do Alimento')),
            ],
        ),
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cadastroprod', models.DateField(auto_now_add=True, verbose_name='Data de cadastro de produto')),
                ('abastecimento', models.DateField(auto_now=True, verbose_name='Data de abastecimento do estoque')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20, verbose_name='Nome')),
                ('Descricao', models.CharField(max_length=200, verbose_name='Descrição')),
                ('codigo', models.CharField(max_length=5, verbose_name='Código')),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do fornecedor')),
                ('Endereco', models.CharField(max_length=100, verbose_name='Endereço')),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, verbose_name='Nome do Funcionario')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('senha', models.CharField(max_length=256, verbose_name='Senha')),
                ('tipo', models.CharField(max_length=15, verbose_name='Tipo')),
                ('matricula', models.CharField(max_length=9, verbose_name='Matrícula')),
            ],
        ),
        migrations.CreateModel(
            name='ValidadedeAlimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataValidade', models.DateField(verbose_name='Data')),
                ('quantidade', models.FloatField(verbose_name='Quantidade recebida')),
                ('nomeAlimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginas.alimento')),
            ],
        ),
        migrations.CreateModel(
            name='Utiliza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turno', models.CharField(max_length=15, verbose_name='Turno utilizou')),
                ('data', models.DateField(verbose_name='Data que o alimento foi utilizado')),
                ('quantidade', models.FloatField(verbose_name='Quantidade utilizada')),
                ('matriculaFuncionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginas.funcionario')),
                ('nomeAlimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginas.alimento')),
            ],
        ),
        migrations.CreateModel(
            name='TelefoneFornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(max_length=11, verbose_name='Telefone')),
                ('cnpjFornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginas.fornecedor')),
            ],
        ),
        migrations.CreateModel(
            name='Recebe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.FloatField(verbose_name='Quantidade recebida')),
                ('data', models.DateField(verbose_name='Data de recebimento')),
                ('matriculaFuncionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginas.funcionario')),
                ('nomeAlimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginas.alimento')),
            ],
        ),
        migrations.CreateModel(
            name='Fornece',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpjFornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginas.fornecedor')),
                ('nomeAlimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginas.alimento')),
            ],
        ),
    ]
