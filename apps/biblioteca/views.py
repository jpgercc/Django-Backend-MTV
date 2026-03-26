from django.shortcuts import render
from biblioteca.models import Biblioteca
from rest_framework import viewsets
from biblioteca.serializer import BibliotecaSerializer

# Create your views here.


# Após o comentario "# Create your views here." e crie as views "Biblioteca".

class BibliotecaViewSet(viewsets.ModelViewSet):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializer  