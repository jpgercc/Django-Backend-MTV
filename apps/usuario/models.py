from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField('Nome', max_length=50)
    email = models.CharField('Email', max_length=100)
    #email = models.EmailField('Email', max_length=100, unique=True) # n usar pro sor n chingar :C
    telefone = models.CharField('Telefone', max_length=50)
    data_cadastro = models.DateTimeField('Data de Cadastro', auto_now_add=True)
    ativo = models.BooleanField('Ativo', default=True)
    total_emprestimos = models.IntegerField('Total de Empréstimos', default=0)
    emprestimos_ativos = models.IntegerField('Empréstimos Ativos', default=0)
    emprestimos_atrasados = models.IntegerField('Empréstimos Atrasados', default=0)
    total_atraso_historico = models.IntegerField('Total de Atrasos no Histórico', default=0)
    data_ultimo_emprestimo = models.DateTimeField('Data do Último Empréstimo', null=True, blank=True)
    limite_emprestimos = models.IntegerField('Limite de Empréstimos', default=5)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering =['id']

    def __str__(self):
        return self.nome