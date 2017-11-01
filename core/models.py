# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Perfil(models.Model):
    escolaridade_choices = (
        (1, ("Fundamental")),
        (2, ("Médio")),
        (3, ("Superior Incompleto")),
        (4, ("Superior Completo"))
    )
    pretensao_minima = models.DecimalField("Pretensão Mínima", max_digits=10,
                                           decimal_places=2, default=1000.00)
    pretensao_maxima = models.DecimalField("Pretensão Máxima", max_digits=10,
                                           decimal_places=2, default=1000.00)
    experiencia = models.IntegerField("Experiência", default=1)
    escolaridade = models.IntegerField("Escolaridade",
                                       choices=escolaridade_choices,
                                       default=1)
    distancia = models.IntegerField("Distância", default=10)

    class Meta:
        abstract = True


class PerfilCandidato(Perfil):
    candidato = models.OneToOneField(User)


class Vaga(Perfil):
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField("Nome da Vaga", max_length=100)

    def get_absolute_url(self):
        return reverse('vaga', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('vaga_delete', args=[str(self.id)])


class Candidatura(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, default=1)
    candidato = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('candidatura', args=[str(self.id)])
