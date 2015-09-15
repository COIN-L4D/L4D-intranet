# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0003_auto_20150915_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='template_file',
            field=models.CharField(max_length=256, verbose_name=b'The template used for this page'),
        ),
    ]
