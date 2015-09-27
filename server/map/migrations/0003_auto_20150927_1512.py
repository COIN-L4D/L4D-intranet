# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20150926_1423'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapevent',
            name='time',
        ),
        migrations.AddField(
            model_name='mapevent',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 15, 12, 49, 135986, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
