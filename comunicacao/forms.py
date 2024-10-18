from django import forms
from .models import Mensagem

class FormularioTeste(forms.ModelForm):
    class Meta:
        model = Mensagem
        fields = ['nome', 'email', 'mensagem']
