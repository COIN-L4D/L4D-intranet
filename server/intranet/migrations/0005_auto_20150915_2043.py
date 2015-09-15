# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0004_auto_20150915_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagepassword',
            name='page',
            field=models.OneToOneField(verbose_name=b'The target page of the link', to='intranet.Page'),
        ),
        migrations.AlterField(
            model_name='pagepassword',
            name='password',
            field=models.CharField(unique=True, max_length=128, verbose_name=b'The secret code to type to reveal the page'),
        ),
        migrations.AlterField(
            model_name='visiblepage',
            name='page',
            field=models.OneToOneField(to='intranet.Page'),
        ),
    ]
