from django.contrib.auth import get_user_model
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.views import View

from .models import Cadastro
from .forms import CadastroForm
from django.urls import reverse_lazy

from django.views.generic import (
        ListView,
        UpdateView,
        DeleteView,
        CreateView,
        DetailView
        )
#------------------------------------------------------- CHARTS
from rest_framework.views import APIView
from rest_framework.response import Response
#-------------------------------------------------------

def dashboard(request):
    return render(request, 'dashboard/index.html')

class CadastroNovo(CreateView):
    model = Cadastro
    form_class = CadastroForm


class Cadastrolist(ListView):
    model = Cadastro

class CadastroDelete(DeleteView):
    model = Cadastro
    success_url = reverse_lazy('list_cadastro')


class CadastroDetail(DetailView):
    model = Cadastro

class CadastroEditar(UpdateView):
    model = Cadastro
    form_class = CadastroForm   


def my_logout(request):
    logout(request)
    return redirect('dashboard')

#------------------------------------------------------
# User = get_user_model()


def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data)

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        total_cadastros = Cadastro.objects.all().count()
        total_homens = Cadastro.objects.filter(sexo="MASCULINO").count()
        total_mulheres = Cadastro.objects.filter(sexo="FEMININO").count()
        total_casado = Cadastro.objects.filter(estadocivil="CASADO(A)").count()
        labels = ['Cadastros', 'Homens', 'Mulheres', 'Casados']
        default_items = [total_cadastros, total_homens, total_mulheres, total_casado]
        data = {
            "labels": labels,
            "default": default_items,
        }
        return Response(data)