from django.shortcuts import render
from rest_framework import viewsets
from livro.models import Livro
from livro.serializer import LivroSerializer
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
# Após o comentario "# Create your views here." e crie as views "Category".

class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer  