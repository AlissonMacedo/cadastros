from django import forms
from .models import *

#-------- Aluno Form -------------------------------------


class CadastroForm(forms.ModelForm):
    
    datadenascimento = forms.DateInput(format=('%d-%m-%Y'), attrs={'type':'date'})
    class Meta:
        model = Cadastro
        fields = ['nomecompleto','datadenascimento',
            'etinia','estadocivil','sexo',
            'religiao', 'filhos', 'filhosmaiores',
            'filhosmenores', 'graudeinstrucao', 'cep', 'rua',
            'numero', 'bairro', 'cidade', 'uf', 'ibge', 
            'telefone', 'hipotesedig', 'atemdimento', 'retornoum',
            'retornodois', 'obs', 'filhossn', 'profissao']
