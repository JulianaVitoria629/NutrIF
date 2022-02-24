from django.contrib import admin

from paginas.models import Alimento, Categoria, Fornecedor, Funcionario, TelefoneFornecedor, ValidadedeAlimento
admin.site.register(Funcionario)
admin.site.register(Alimento)
admin.site.register(Fornecedor)
admin.site.register(Categoria)
admin.site.register(ValidadedeAlimento)
admin.site.register(TelefoneFornecedor)
