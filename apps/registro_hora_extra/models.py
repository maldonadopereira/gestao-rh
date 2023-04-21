from django.db import models


class RegistroHoraExtra(models.Model):
    motivo = models.CharField('Motivo', max_length=100)

    class Meta:
        verbose_name = 'Registro de Hora Extra'
        verbose_name_plural = 'Registros de Hora Extra'

    def __str__(self):
        return self.motivo