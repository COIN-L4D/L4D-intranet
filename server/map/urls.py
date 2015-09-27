from django.conf.urls import url

from .api import GetMapEventsAPI, PushMapEventAPI

urlpatterns = [
    url('^events$', GetMapEventsAPI.as_view(), name='map-get-events'),
    url('^push$', PushMapEventAPI.as_view(), name='map-push-event'),
]
