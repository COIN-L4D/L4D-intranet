# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='path',
        ),
        migrations.AddField(
            model_name='page',
            name='url_name',
            field=models.TextField(verbose_name=b'The name used in the url', blank=True),
        ),
    ]
