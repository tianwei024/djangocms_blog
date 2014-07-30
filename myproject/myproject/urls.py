#coding=utf-8

# from django.conf.urls import patterns, include, url
#
# from django.contrib import admin
# admin.autodiscover()
#
# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'myproject.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     url(r'^admin/', include(admin.site.urls)),
# )

from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)

if settings.DEBUG:
    urlpatterns = patterns('',
        (r'^' + settings.MEDIA_URL.lstrip('/'), include('appmedia.urls')),
    ) + urlpatterns