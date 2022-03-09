from dataclasses import fields
from django import forms

from paginas.models import Funcionario
from django.core.mail.message import EmailMessage
from . import UserCreationForm


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__' 
class UsercreationForm(forms.Model):
    