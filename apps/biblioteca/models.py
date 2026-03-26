from django.db import models
#from exemplar.models import Exemplar
#from funcionario.models import Funcionario

########################################################################################
# Conferir relaçoes ManyToManyField comentadas no final e imports no inicio do arquivo #
########################################################################################

# Após o comentario "# Create your models here." e crie a classe "Biblioteca" do modelo.

class Biblioteca(models.Model):
    nome = models.CharField('Nome completo', max_length=50)
    endereco = models.CharField('Endereço', max_length=200)
    telefone = models.CharField('Telefone', max_length=20)

    # não precisa declarar "catalogo" aqui, ele será criado automaticamente pelo related_name de Livro:
#    class Livro(models.Model):
#        titulo = models.CharField(max_length=100)
#        autor = models.CharField(max_length=100)
#        biblioteca = models.ForeignKey(
#            Biblioteca,
#            on_delete=models.CASCADE,
#            related_name='catalogo'   # <<< equivalente ao List<Livro>
#        )



    #catalogo = models.ManyToManyField('Livro', related_name='bibliotecas') # se um livro pode estar em varias bibliotecas
    #funcionario = models.ManyToManyField(Funcionario, verbose_name="Funcionario")
    #exemplar = models.ManyToManyField(Exemplar, verbose_name="Exemplar")
    class Meta:
        verbose_name = 'Biblioteca'
        verbose_name_plural = 'Bibliotecas'
        ordering =['id']

    def __str__(self):
        return self.nome
