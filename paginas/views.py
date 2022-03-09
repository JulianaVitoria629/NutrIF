from audioop import reverse
from dataclasses import fields
from re import template
from django.shortcuts import redirect, render
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
    template_name = 'cadastros/form.html'

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
    template_name = 'cadastros/form.html'
    sucess_url = reverse_lazy('index')

def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('index')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'cadastro.html', {'form_usuario': form_usuario})
