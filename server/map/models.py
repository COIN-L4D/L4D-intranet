from django.db import models

import datetime

class MapSettings(models.Model):

    center_lat = models.FloatField(default=50.609301)
    center_lng = models.FloatField(default=3.142074)
    initial_zoom = models.FloatField(default=15)
    event_life_time = models.FloatField(
        default=datetime.timedelta(minutes=20).total_seconds(),
        help_text='in number of seconds'
    )

    @staticmethod
    def get_settings():
        settings, created =  MapSettings.objects.get_or_create()
        return settings

class MapEvent(models.Model):
    """ Model for an event on the map """
    datetime = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()

    def __str__(self):
        return self.text

    def __unicode__(self):
        return self.__str__()
