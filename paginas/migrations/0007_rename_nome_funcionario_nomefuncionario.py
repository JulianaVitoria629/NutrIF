# Generated by Django 4.0.1 on 2022-03-16 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0006_alter_categoria_descricao_alter_fornecedor_endereco'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='nome',
            new_name='nomeFuncionario',
        ),
    ]