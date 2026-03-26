from django.db import models

# Create your models here.
# Após o comentario "# Create your models here." e crie a classe "Autor" do modelo.

class Autor(models.Model):
    nome = models.CharField('Nome', max_length=50)

    #nacionalidade = models.CharField('Nacionalidade', max_length=30)
    NACIONALIDADE_CHOICES = [
        ('DE', 'Alemão'),
        ('AR', 'Argentino'),
        ('AU', 'Australiano'),
        ('BE', 'Belga'),
        ('BR', 'Brasileiro'),
        ('BG', 'Búlgaro'),
        ('CA', 'Canadense'),
        ('CN', 'Chinês'),
        ('CZ', 'Tcheco'),
        ('DK', 'Dinamarquês'),
        ('ES', 'Espanhol'),
        ('US', 'Estadunidense'),
        ('FI', 'Finlandês'),
        ('FR', 'Francês'),
        ('GR', 'Grego'),
        ('NL', 'Holandês'),
        ('HU', 'Húngaro'),
        ('IE', 'Irlandês'),
        ('IN', 'Indiano'),
        ('IT', 'Italiano'),
        ('JP', 'Japonês'),
        ('KR', 'Sul-Coreano'),
        ('MX', 'Mexicano'),
        ('NO', 'Norueguês'),
        ('PT', 'Português'),
        ('PL', 'Polonês'),
        ('RO', 'Romeno'),
        ('RU', 'Russo'),
        ('ZA', 'Sul-Africano'),
        ('CH', 'Suíço'),
        ('SE', 'Sueco'),      # Corrigido: código SA é Arábia Saudita — alterado para SE (Suécia)
        ('TR', 'Turco'),
        ('OT', 'Outro'),
    ]

    nacionalidade = models.CharField('Nacionalidade', max_length=3, choices=NACIONALIDADE_CHOICES)
    data_nascimento = models.DateField('Data de Nascimento')

    #sexo = models.CharField('Sexo', max_length=10)
    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES)
    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering =['id']

    def __str__(self):
        return self.nome