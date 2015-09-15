# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0002_auto_20150915_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(unique=True, max_length=64, verbose_name=b'An explicit name of the page'),
        ),
        migrations.AlterField(
            model_name='page',
            name='url_name',
            field=models.CharField(unique=True, max_length=64, verbose_name=b'The name used in the url'),
        ),
    ]
