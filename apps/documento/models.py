from django.db import models
from apps.funcionario.models import Funcionario


class Documento(models.Model):
    descricao = models.CharField('Descrição', max_length=100)
    proprietario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural = 'Descrições'

    def __str__(self):
        return self.descricao