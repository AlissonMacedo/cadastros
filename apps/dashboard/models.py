from django.db import models
from django import forms
from django.urls import reverse

#-------- Cadastro Model -------------------------------------


class Cadastro(models.Model):
    id = models.AutoField(primary_key=True)
    numeroficha = models.IntegerField( 'Nº Ficha')
    nomecompleto = models.CharField('Nome Completo', max_length=60)
    datadenascimento = models.DateTimeField('Data Nascimento', max_length=10, blank=True, null=True)
    etinia = models.CharField('Etinia', max_length=30, blank=True, null=True)
    religiao = models.CharField('Religião', max_length=60, blank=True, null=True)
    filhosmaiores = models.IntegerField('Filhos Maiores de Idade', blank=True, null=True)
    filhosmenores = models.IntegerField('Filhos Menores de Idade', blank=True, null=True)
    graudeinstrucao = models.CharField('Grau de Instrução', max_length=60, blank=True, null=True)
    cep = models.CharField(max_length=10, blank=True, null=True)
    rua = models.CharField(max_length=60, blank=True, null=True)
    numero = models.IntegerField('Numero', blank=True, null=True)
    bairro = models.CharField(max_length=40, blank=True, null=True)
    cidade = models.CharField(max_length=40, blank=True, null=True)
    ibge = models.CharField(max_length=8, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    uf = models.CharField(max_length=2, blank=True, null=True)
    telefone = models.CharField(max_length=15)
    hipotesedig = models.CharField('Hipótese Diagnóstica:', max_length=100, blank=True, null=True)
    atemdimento = models.CharField('Atendimento:', max_length=100, blank=True, null=True)
    retornoum = models.CharField('Retorno 1:', max_length=100, blank=True, null=True)
    retornodois = models.CharField('Retorno 2:', max_length=100, blank=True, null=True)
    obs = models.CharField('Obs:', max_length=100, blank=True, null=True)
    profissao = models.CharField('Profissao', max_length=60, blank=True, null=True)
    

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
