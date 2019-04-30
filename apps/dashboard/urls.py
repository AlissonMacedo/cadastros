from django.conf.urls import url, include
from django.contrib import admin
from .views import *
from django.urls import path

from django.urls import include, path


#---- URLs Core -------------------------------------------------------------

urlpatterns = [

    path('', dashboard, name='dashboard'),
    path('novo-cadastro/', CadastroNovo.as_view(), name='cadastro'),
    path('listar-cadastro/', Cadastrolist.as_view(), name='list_cadastro'),
    path('editar-cadastro/<int:pk>', CadastroEditar.as_view(), name='editar_cadastro'),
    path('deletar-cadastro/<int:pk>', CadastroDelete.as_view(), name='deletar_cadastro'),
    path('detalhe-cadastro/<int:pk>/', CadastroDetail.as_view(), name='detalhe_cadastro'),
    path('logout/', my_logout, name='mylogout'),

    path('api/chart/data/', ChartData.as_view())

    
]
