from django.db import models
#from products.models import Product
#from orders.models import Order
from autor.models import Autor
from editora.models import Editora
#from exemplar.models import Exemplar
# Create your models here.

# Após o comentario "# Create your models here." e crie a classe "Livro" do modelo.

class Livro(models.Model):
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    title = models.CharField('Título', max_length=200)
    ano_publicacao = models.PositiveIntegerField('Ano de Publicação')
    edicao = models.CharField('Edição', max_length=50)
    sinopse = models.TextField('Sinopse', blank=True, null=True)
    capa_url = models.URLField('URL da Capa', blank=True, null=True) # segundo o diagrama era para ser tipo String
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name='Autor')
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE, verbose_name='Editora')

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'
        ordering =['id']

    def __str__(self):
        return f"{self.title} - {self.autor} - {self.editora}"