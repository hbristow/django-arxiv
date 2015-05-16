# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from django.core.management import call_command

def load_fixtures(*args):
    call_command('loaddata', 'subjects.json', app='arxiv')

class Migration(migrations.Migration):

    dependencies = [
        ('arxiv', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixtures),
    ]
