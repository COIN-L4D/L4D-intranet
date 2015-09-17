from django.conf.urls import url

from .views import (
    HomeView, ClosedView, PageView, DeniedView
)

from .api import (
    MenuAPI, TryPasswordAPI
)

urlpatterns = [
    url('^api/menu$', MenuAPI.as_view(), name='menu'),
    url('^api/try$', TryPasswordAPI.as_view(), name='try'),

    url('^page/(?P<url_name>.*)', PageView.as_view(), name='page'),
    url('^closed$', ClosedView.as_view(), name='closed'),
    url('^denied$', DeniedView.as_view(), name='denied'),

    url('^$', HomeView.as_view(), name='home'),
]
