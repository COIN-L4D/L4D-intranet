from django.conf.urls import url

from intranet.views import (
    HomeView, ClosedView, PageView, DeniedView
)

from intranet.api import (
    StartAPI, PauseAPI, StopAPI, RestartAPI,
    MenuAPI, TryPasswordAPI
)

urlpatterns = [
    url('^api/start$', StartAPI.as_view(), name='start'),
    url('^api/pause$', PauseAPI.as_view(), name='pause'),
    url('^api/stop$', StopAPI.as_view(), name='stop'),
    url('^api/restart$', RestartAPI.as_view(), name='restart'),

    url('^api/menu$', MenuAPI.as_view(), name='menu'),
    url('^api/try$', TryPasswordAPI.as_view(), name='try'),

    url('^page/(?P<url_name>.*)', PageView.as_view(), name='page'),
    url('^closed$', ClosedView.as_view(), name='closed'),
    url('^denied$', DeniedView.as_view(), name='denied'),

    url('^$', HomeView.as_view(), name='home'),
]
