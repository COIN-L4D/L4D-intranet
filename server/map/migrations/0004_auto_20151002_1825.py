# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_auto_20150927_1512'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mapevent',
            old_name='text',
            new_name='description',
        ),
        migrations.AddField(
            model_name='mapevent',
            name='event_type',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mapevent',
            name='title',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
