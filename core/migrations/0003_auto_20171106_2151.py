# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20171031_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilcandidato',
            name='distancia',
            field=models.IntegerField(default=10, verbose_name=b'Dist\xc3\xa2ncia'),
        ),
        migrations.AlterField(
            model_name='perfilcandidato',
            name='escolaridade',
            field=models.IntegerField(default=1, verbose_name=b'Escolaridade', choices=[(1, b'Fundamental'), (2, b'M\xc3\xa9dio'), (3, b'Superior Incompleto'), (4, b'Superior Completo')]),
        ),
        migrations.AlterField(
            model_name='perfilcandidato',
            name='experiencia',
            field=models.IntegerField(default=1, verbose_name=b'Experi\xc3\xaancia'),
        ),
        migrations.AlterField(
            model_name='perfilcandidato',
            name='pretensao_maxima',
            field=models.DecimalField(default=1000.0, verbose_name=b'Pretens\xc3\xa3o M\xc3\xa1xima', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='perfilcandidato',
            name='pretensao_minima',
            field=models.DecimalField(default=1000.0, verbose_name=b'Pretens\xc3\xa3o M\xc3\xadnima', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='distancia',
            field=models.IntegerField(default=10, verbose_name=b'Dist\xc3\xa2ncia'),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='escolaridade',
            field=models.IntegerField(default=1, verbose_name=b'Escolaridade', choices=[(1, b'Fundamental'), (2, b'M\xc3\xa9dio'), (3, b'Superior Incompleto'), (4, b'Superior Completo')]),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='experiencia',
            field=models.IntegerField(default=1, verbose_name=b'Experi\xc3\xaancia'),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='nome',
            field=models.CharField(max_length=100, verbose_name=b'Nome da Vaga'),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='pretensao_maxima',
            field=models.DecimalField(default=1000.0, verbose_name=b'Pretens\xc3\xa3o M\xc3\xa1xima', max_digits=10, decimal_places=2),
        ),
        migrations.AlterField(
            model_name='vaga',
            name='pretensao_minima',
            field=models.DecimalField(default=1000.0, verbose_name=b'Pretens\xc3\xa3o M\xc3\xadnima', max_digits=10, decimal_places=2),
        ),
    ]
