from django.conf.urls import url

from intranet.views import (
    HomeView, ClosedView, PageView, DeniedView, AdminView
)

from intranet.api import (
    StartAPI, PauseAPI, StopAPI, RestartAPI,
    MenuAPI, TryPasswordAPI, StatusAPI
)

urlpatterns = [
    url('^api/start$', StartAPI.as_view(), name='start'),
    url('^api/pause$', PauseAPI.as_view(), name='pause'),
    url('^api/stop$', StopAPI.as_view(), name='stop'),
    url('^api/restart$', RestartAPI.as_view(), name='restart'),
    url('^api/status$', StatusAPI.as_view(), name='status'),

    url('^api/menu$', MenuAPI.as_view(), name='menu'),
    url('^api/try$', TryPasswordAPI.as_view(), name='try'),

    url('^game-admin$', AdminView.as_view(), name='game-admin'),

    url('^page/(?P<url_name>.*)', PageView.as_view(), name='page'),
    url('^closed$', ClosedView.as_view(), name='closed'),
    url('^denied$', DeniedView.as_view(), name='denied'),

    url('^$', HomeView.as_view(), name='home'),
]
