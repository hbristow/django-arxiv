# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailServer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=128, verbose_name=b'Email Address')),
                ('host', models.CharField(max_length=64, verbose_name=b'SMTP Hostname')),
                ('port', models.IntegerField(default=25, verbose_name=b'Port Number')),
                ('username', models.CharField(max_length=64, verbose_name=b'Username')),
                ('password', models.CharField(max_length=64, verbose_name=b'Password')),
                ('tls', models.BooleanField(default=False, verbose_name=b'TLS')),
                ('ssl', models.BooleanField(default=False, verbose_name=b'SSL')),
            ],
            options={
                'verbose_name': 'Mail Server Configuration',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timezone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('region', models.CharField(max_length=64, verbose_name=b'Region')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name=b'Name')),
                ('cat', models.CharField(max_length=64, verbose_name=b'Category Code')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=128, verbose_name=b'Email Address')),
                ('uuid', models.CharField(verbose_name=b'Universal Identifier', max_length=32, editable=False, blank=True)),
                ('timezone', models.ForeignKey(to='arxiv.Timezone')),
                ('subjects', models.ManyToManyField(to='arxiv.Subject')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
