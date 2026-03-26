from django.shortcuts import render
from rest_framework import viewsets
from usuario.models import Usuario
from usuario.serializer import UsuarioSerializer

# Create your views here.
# Após o comentario "# Create your views here." e crie as views "Category".

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer  