# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentGame',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('state', models.CharField(default=b'S', max_length=2, verbose_name=b'The state of the current game', choices=[(b'R', b'Run'), (b'P', b'Pause'), (b'S', b'Stop')])),
                ('start_datetime', models.DateTimeField(verbose_name=b'The datetime when the last game has started')),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64, verbose_name=b'An explicit name of the page')),
                ('path', models.TextField(verbose_name=b'The path of the page used in the URL', blank=True)),
                ('template_file', models.TextField(verbose_name=b'The template used for this page')),
                ('initially_visible', models.BooleanField(default=False, verbose_name=b'The page is it visible at the start of the game')),
            ],
        ),
        migrations.CreateModel(
            name='PagePassword',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name=b'The secret code to type to reveal the page')),
                ('page', models.ForeignKey(verbose_name=b'The target page of the link', to='intranet.Page')),
            ],
        ),
        migrations.CreateModel(
            name='VisiblePage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('page', models.ForeignKey(to='intranet.Page')),
            ],
        ),
    ]
