from django.conf.urls import *
from django.conf.urls import patterns, include, url

from django.contrib import admin
from apps import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Appserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),



    url(r'^contact/$', views.index),

    url(r'^admin/', include(admin.site.urls)),
)
