from django.db import models


class Documento(models.Model):
    descricao = models.CharField('Descrição', max_length=100)

    class Meta:
        verbose_name_plural = 'Descrições'

    def __str__(self):
        return self.descricao