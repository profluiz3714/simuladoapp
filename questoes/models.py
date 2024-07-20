# questoes/models.py

from django.db import models
from ckeditor.fields import RichTextField

class Questao(models.Model):
    enunciado = RichTextField()
    disciplina = models.CharField(max_length=100)
    gabarito = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)

    def __str__(self):
        return self.enunciado
