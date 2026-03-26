from django.shortcuts import render
from autor.models import Autor
from rest_framework import viewsets
from autor.serializer import AutorSerializer

# Create your views here.
# Após o comentario "# Create your views here." e crie as views "Autor".
class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer  