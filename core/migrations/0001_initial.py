# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidatura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('candidato', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PerfiCandidato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pretensao_minima', models.DecimalField(default=1000.0, max_digits=10, decimal_places=2)),
                ('pretensao_maxima', models.DecimalField(default=1000.0, max_digits=10, decimal_places=2)),
                ('experiencia', models.IntegerField(default=1)),
                ('escolaridade', models.IntegerField(default=1, choices=[(1, b'Fundamental'), (2, b'M\xc3\xa9dio'), (3, b'Superior Incompleto'), (4, b'Superior Completo')])),
                ('distancia', models.IntegerField(default=10)),
                ('candidato', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pretensao_minima', models.DecimalField(default=1000.0, max_digits=10, decimal_places=2)),
                ('pretensao_maxima', models.DecimalField(default=1000.0, max_digits=10, decimal_places=2)),
                ('experiencia', models.IntegerField(default=1)),
                ('escolaridade', models.IntegerField(default=1, choices=[(1, b'Fundamental'), (2, b'M\xc3\xa9dio'), (3, b'Superior Incompleto'), (4, b'Superior Completo')])),
                ('distancia', models.IntegerField(default=10)),
                ('nome', models.CharField(max_length=100)),
                ('empresa', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='candidatura',
            name='vaga',
            field=models.ForeignKey(default=1, to='core.Vaga'),
        ),
    ]
