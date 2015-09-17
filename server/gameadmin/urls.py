from django.conf.urls import url

from .views import AdminView

from .api import (
    StartAPI, PauseAPI, StopAPI, RestartAPI, StatusAPI
)

urlpatterns = [
    url('^api/start$', StartAPI.as_view(), name='start'),
    url('^api/pause$', PauseAPI.as_view(), name='pause'),
    url('^api/stop$', StopAPI.as_view(), name='stop'),
    url('^api/restart$', RestartAPI.as_view(), name='restart'),
    url('^api/status$', StatusAPI.as_view(), name='status'),

    url('^game-admin$', AdminView.as_view(), name='game-admin'),
]
