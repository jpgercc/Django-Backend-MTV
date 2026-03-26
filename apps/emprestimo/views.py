from django.shortcuts import render
from emprestimo.models import Emprestimo
from rest_framework import viewsets
from emprestimo.serializer import EmprestimoSerializer

# Create your views here.


# Após o comentario "# Create your views here." e crie as views "Emprestimo".

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer  