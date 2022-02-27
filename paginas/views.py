from audioop import reverse
from dataclasses import fields
from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Alimento, Categoria, Fornecedor, Funcionario
# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

class LoginUserView(TemplateView):
    template_name = 'pages-login-user.html'

class RegisterAlimentoView(TemplateView):
    template_name = 'pages-register-alimento.html'

class RegisterUserView(TemplateView):
    template_name = 'pages-register-user.html'

class RegisterView(TemplateView):
    template_name = 'pages-register.html'

class AlimentoCreateView(CreateView): 
    model = Alimento
    fields = ['nome', 'Unidade de medida', 'Código da categoria do alimento']
    template_name = 'pages-register-alimento.html'
    sucess_url = reverse_lazy('index')

class CategoriacreateView(CreateView):
    model = Categoria
    fields = ['nome', 'descrição', 'código']
    template_name = 'pages-register-alimento.html'
    sucess_url = reverse_lazy('index')
    
class FornecedorCreateView(CreateView):
    model = Fornecedor
    fields =['nome', 'endereço', 'cnpj']
    template_name = 'form_fornecedor.html'
    sucess_url = reverse_lazy('index')

class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields =['nome', 'telefone', 'tipo', 'senha', 'matricula']
    template_name = 'pages-register-user.html'
    sucess_url = reverse_lazy('index')
