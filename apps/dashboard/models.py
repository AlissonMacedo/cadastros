from django.db import models
from django import forms
from django.urls import reverse

#-------- Cadastro Model -------------------------------------


class Cadastro(models.Model):
    id = models.AutoField(primary_key=True)
    nomecompleto = models.CharField('Nome Completo', max_length=60)
    datadenascimento = models.DateTimeField('Data Nascimento', max_length=10)
    etinia = models.CharField('Etinia', max_length=30)
    religiao = models.CharField('Religião', max_length=60)
    filhosmaiores = models.IntegerField('Filhos Maiores de Idade')
    filhosmenores = models.IntegerField('Filhos Menores de Idade')
    graudeinstrucao = models.CharField('Grau de Instrução', max_length=60)
    cep = models.CharField(max_length=10)
    rua = models.CharField(max_length=60)
    numero = models.IntegerField('Numero')
    bairro = models.CharField(max_length=40)
    cidade = models.CharField(max_length=40)
    uf = models.CharField(max_length=2)
    ibge = models.CharField(max_length=8, blank=True, null=True)
    telefone = models.CharField(max_length=16, null=True, blank=True)
    hipotesedig = models.CharField('Hipótese Diagnóstica:', max_length=100)
    atemdimento = models.CharField('Atendimento:', max_length=100)
    retornoum = models.CharField('Retorno 1:', max_length=100)
    retornodois = models.CharField('Retorno 2:', max_length=100)
    obs = models.CharField('Obs:', max_length=100)
    profissao = models.CharField('Profissao', max_length=60)

    FILHOSSN_CHOICES = (
    ("-----", "-----"),
    ("SIM", "Sim"),
    ("NÃO", "Não")
    )

    filhossn = models.CharField('Filhos?',max_length=9,
                  choices=FILHOSSN_CHOICES,
                  default="-----")

    ESTADOCIVIL_CHOICES = (
    ("-----", "-----"),
    ("SOLTEIRO(A)", "Solteiro(a)"),
    ("CASADO(A)", "Casado(a)")
    )

    estadocivil = models.CharField(max_length=11,
                  choices=ESTADOCIVIL_CHOICES,
                  default="-----")
    
    FILHOS_CHOICES = (
    ('NÃO', 'Não'),('1', '1'),
    ('2', '2'),('3', '3'),
    ('4 OU MAIS', '4 ou mais'))

    filhos = models.CharField('Qnts',max_length=9,
                  choices=FILHOS_CHOICES,
                  default="NÃO")


    SEXO_CHOICES=[('----','----'),
         ('MASCULINO','Masculino'),
         ('FEMININO','Feminino')]
    
    sexo = models.CharField('Sexo:',max_length=9,
                  choices=SEXO_CHOICES,
                  default="----")

    def get_absolute_url(self):
        return reverse('list_cadastro')

    class Meta:
        verbose_name = 'Cadastro'
        verbose_name_plural = 'Cadastro'
        ordering = ['id']

    def __str__(self):
        return self.id + ' ' + self.nomecompleto + ' ' + self.datadenascimento + ' ' + self.estadocivil
