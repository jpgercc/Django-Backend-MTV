from django.db import models
from biblioteca.models import Biblioteca
from livro.models import Livro
# Create your models here.

# Após o comentario "# Create your models here." e crie a classe "Exemplar" do modelo.
class Exemplar(models.Model):
# q: como deixar um default value em exemplar?
#r: 
    codigo_de_barras = models.CharField(max_length=100, unique=True)
    data_aquisicao = models.DateField('Data de Aquisição')
    estado_de_convervacao = models.CharField('Estado de Conservação', max_length=100)
    preco_de_compra = models.DecimalField('Preço de Compra', max_digits=10, decimal_places=2)
    localizacao = models.CharField('Localização', max_length=100)
    disponivel = models.BooleanField('Disponível', default=True)
    observacoes = models.TextField('Observações', blank=True, null=True)
    foto_capa = models.ImageField(upload_to='exemplar_covers/', blank=True, null=True, verbose_name='Foto da Capa') #extra/ fora do escopo da modelagem
    
    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE, verbose_name='Biblioteca')
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, verbose_name='Livro', null=True)
    class Meta:
        verbose_name = 'Exemplar'
        verbose_name_plural = 'Exemplares'
        ordering =['id']

    def __str__(self):
        return self.codigo_de_barras - self.livro.titulo