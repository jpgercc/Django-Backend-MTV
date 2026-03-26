from django.db import models
from usuario.models import Usuario
from funcionario.models import Funcionario
from exemplar.models import Exemplar

# Create your models here.

# Após o comentario "# Create your models here." e crie a classe "Order" do modelo.
class Emprestimo(models.Model):
    data_emprestimo = models.DateField('Data de Empréstimo')
    data_devolucao_prevista = models.DateField('Data de Devolução Prevista')
    data_devolucao = models.DateField('Data de Devolução')
    status = models.CharField('Status', max_length=20)
    renovacoes_realizadas = models.IntegerField('Renovações Realizadas', default=0)
    max_renovacoes = models.IntegerField('Máximo de Renovações', default=2)
    
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    exemplar = models.ForeignKey(Exemplar, on_delete=models.CASCADE, null=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

    exemplares_renovados = models.ManyToManyField(Exemplar, related_name='emprestimos_renovados', blank=True)

    #q: boa ideia, renovados como many to many, mas esse campo nao existem em exemplar.models.py tem problema?
    #r: Não há problema em ter um ManyToManyField em um modelo que se refere a outro modelo, mesmo que o campo correspondente não exista no outro modelo. O Django gerencia essas relações automaticamente. No entanto, é importante garantir que a lógica do seu aplicativo lide corretamente com essas relações.

    

    class Meta:
        verbose_name = 'Emprestimo'
        verbose_name_plural = 'Emprestimos'
        ordering =['id']

    def __str__(self):
        return f"{self.id} - {self.usuario} - {self.exemplar} - {self.status}" 
