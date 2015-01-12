from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import surgealert.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simpleserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', surgealert.views.index, name='index'),
    url(r'^db', surgealert.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

)
