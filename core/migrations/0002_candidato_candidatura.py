# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('perfil', models.OneToOneField(null=True, blank=True, to='core.PerfilProfissional')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('pode_criar_perfil', 'Pode criar Perfil Profissional'),),
            },
        ),
        migrations.CreateModel(
            name='Candidatura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('candidato', models.ForeignKey(to='core.Candidato')),
                ('vaga', models.ForeignKey(to='core.Vaga')),
            ],
        ),
    ]
