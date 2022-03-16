from dataclasses import fields
from django import forms

from paginas.models import Alimento, Funcionario
from django.core.mail.message import EmailMessage


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

        
class AlimentoForm(forms.ModelForm):
     class Meta:
        model = Alimento
        fields = '__all__'

    