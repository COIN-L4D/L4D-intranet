# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapsettings',
            name='event_life_time',
            field=models.FloatField(default=1200.0, help_text=b'in number of seconds'),
        ),
    ]
