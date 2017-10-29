# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_candidato_candidatura'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilCandidato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('candidato', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameModel(
            old_name='PerfilProfissional',
            new_name='Perfil',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='perfil',
        ),
        migrations.RemoveField(
            model_name='candidato',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='usuariopadrao',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='usuariopadrao',
            name='user_permissions',
        ),
        migrations.AlterField(
            model_name='candidatura',
            name='candidato',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='empresa',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Candidato',
        ),
        migrations.DeleteModel(
            name='Empresa',
        ),
        migrations.DeleteModel(
            name='UsuarioPadrao',
        ),
        migrations.AddField(
            model_name='perfilcandidato',
            name='perfil',
            field=models.OneToOneField(to='core.Perfil'),
        ),
    ]
