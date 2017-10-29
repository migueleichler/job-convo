# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Perfil(models.Model):
    escolaridade_choices = (
        (1, ("Fundamental")),
        (2, ("Médio")),
        (3, ("Superior Incompleto")),
        (4, ("Superior Completo"))
    )
    pretensao_minima = models.DecimalField(max_digits=10, decimal_places=2)
    pretensao_maxima = models.DecimalField(max_digits=10, decimal_places=2)
    experiencia = models.IntegerField()
    escolaridade = models.IntegerField(choices=escolaridade_choices, default=1)
    distancia = models.IntegerField()


# class UsuarioPadrao(AbstractUser):
#     tipo_choices = (
#         (1, ('Empresa')),
#         (2, ('Cliente')),
#     )
#     tipo = models.IntegerField(choices=tipo_choices, default=1)


class PerfilCandidato(models.Model):
    candidato = models.OneToOneField(User)
    perfil = models.OneToOneField(Perfil)


# class Empresa(models.Model):
#     usuario = models.OneToOneField(UsuarioPadrao)
#
#     class Meta:
#         permissions = (
#             ("pode_criar_vaga", "Pode criar Vaga"),
#         )
#
#
# class Candidato(models.Model):
#     usuario = models.OneToOneField(UsuarioPadrao)
#     perfil = models.OneToOneField(PerfilProfissional, blank=True, null=True)
#
#     class Meta:
#         permissions = (
#             ("pode_criar_perfil", "Pode criar Perfil Profissional"),
#         )


class Vaga(models.Model):
    empresa = models.ForeignKey(User, on_delete=models.CASCADE)
    perfil = models.OneToOneField(Perfil)
    nome = models.CharField(max_length=100)


class Candidatura(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    candidato = models.ForeignKey(User, on_delete=models.CASCADE)
