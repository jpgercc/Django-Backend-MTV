from django.db import models
from biblioteca.models import Biblioteca

# Após o comentario "# Create your models here." e crie a classe "Order" do modelo.

class Funcionario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.CharField('Email', max_length=50)
    telefone = models.CharField('Telefone', max_length=15)
    cargo = models.CharField('Cargo', max_length=100)
    data_admissao = models.DateField('Data de Admissão')
    ativo = models.BooleanField('Ativo', default=True)

    biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE, verbose_name='Biblioteca', null=True)
    
    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        ordering =['id']

    def __str__(self):
        return self.nome 
