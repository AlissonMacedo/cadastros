import datetime
from urllib import request

from django import template

from apps.dashboard.models import Cadastro

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag(takes_context=True)
def total_cadastrados(context):
    return len(Cadastro.objects.all())

@register.simple_tag(takes_context=True)
def total_cadastrados_homens(context):
    return len(Cadastro.objects.filter(sexo="MASCULINO"))

@register.simple_tag(takes_context=True)
def total_cadastrados_mulheres(context):
    return len(Cadastro.objects.filter(sexo="FEMININO"))

@register.simple_tag(takes_context=True)
def total_cadastrados_casados(context):
    return len(Cadastro.objects.filter(estadocivil="CASADO(A)"))
