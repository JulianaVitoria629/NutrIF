# Generated by Django 4.0.1 on 2022-03-16 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0002_rename_descricao_categoria_descricao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='descricao',
            field=models.CharField(max_length=200, verbose_name='Descricao'),
        ),
        migrations.AlterField(
            model_name='fornecedor',
            name='endereco',
            field=models.CharField(max_length=100, verbose_name='Endereco'),
        ),
    ]