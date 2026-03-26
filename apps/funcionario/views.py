from django.shortcuts import render
from funcionario.models import Funcionario
from rest_framework import viewsets
from funcionario.serializer import FuncionarioSerializer
# Create your views here.


# Após o comentario "# Create your views here." e crie as views "Funcionario".

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer  