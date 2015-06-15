# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arxiv', '0003_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailserver',
            name='domain',
            field=models.URLField(default='', max_length=128, verbose_name=b'Site Domain'),
            preserve_default=False,
        ),
    ]
