from django.db import models

# Create your models here.
class Editora(models.Model):
    nome = models.CharField('Nome', max_length=50)
    cnpj = models.CharField('CNPJ', max_length=18)
    endereco = models.CharField('Endereço', max_length=100)
    telefone = models.CharField('Telefone', max_length=15)
    
    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'
        ordering =['id']

    def __str__(self):
        return self.nome