
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('login.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #for get functions
    #(r'^articles/', include('articles.urls')),
)
