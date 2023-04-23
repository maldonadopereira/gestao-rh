from django.db import models
from apps.funcionario.models import Funcionario

class RegistroHoraExtra(models.Model):
    motivo = models.CharField('Motivo', max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT, verbose_name='Funcionário')

    class Meta:
        verbose_name = 'Registro de Hora Extra'
        verbose_name_plural = 'Registros de Hora Extra'

    def __str__(self):
        return self.motivo

