from editora.models import Editora
from rest_framework import viewsets
from editora.serializer import EditoraSerializer

# Após o comentario "# Create your views here." e crie as views "Editora".
class EditoraViewSet(viewsets.ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer  