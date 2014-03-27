from django.conf.urls import *
from django.conf.urls import patterns, include, url

from django.contrib import admin
from apps.admin import AppAdmin
from apps import views
from django.core import urlresolvers
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Appserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



    url(r'^contact/$', views.index),

    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    # Serve static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()

    # Serve Media
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    )