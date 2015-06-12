# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arxiv', '0002_subjects'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailserver',
            name='name',
            field=models.CharField(default='', max_length=128, verbose_name=b'From Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mailserver',
            name='email',
            field=models.EmailField(max_length=128, verbose_name=b'From Address'),
        ),
    ]
