from django.shortcuts import render
from exemplar.models import Exemplar
from rest_framework import viewsets
from exemplar.serializer import ExemplarSerializer
# Create your views here.


# Após o comentario "# Create your views here." e crie as views "Exemplar".

class ExemplarViewSet(viewsets.ModelViewSet):
    queryset = Exemplar.objects.all()
    serializer_class = ExemplarSerializer 