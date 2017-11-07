# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20171106_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfilcandidato',
            name='pretensao_maxima',
        ),
        migrations.RemoveField(
            model_name='perfilcandidato',
            name='pretensao_minima',
        ),
        migrations.AddField(
            model_name='perfilcandidato',
            name='pretensao',
            field=models.DecimalField(default=1000.0, verbose_name=b'Pretens\xc3\xa3o Salarial', max_digits=10, decimal_places=2),
        ),
    ]
