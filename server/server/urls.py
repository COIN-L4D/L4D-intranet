from django.conf.urls import include, url
from django.contrib import admin
from intranet import urls as intranet_urls
from gameadmin import urls as gameadmin_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^', include(intranet_urls)),
    url(r'^', include(gameadmin_urls)),
]
