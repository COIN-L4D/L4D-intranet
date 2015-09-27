# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MapEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='MapSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('center_lat', models.FloatField(default=50.609301)),
                ('center_lng', models.FloatField(default=3.142074)),
                ('initial_zoom', models.FloatField(default=15)),
                ('event_life_time', models.TimeField(default=datetime.timedelta(0, 1200))),
            ],
        ),
    ]
