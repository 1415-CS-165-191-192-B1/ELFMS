from django.conf.urls import patterns, url

from requestManager import views

urlpatterns = patterns('',
    url(r'^$', views.reqManager, name='request'),
    url(r'^(?P<resource_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^create/$', views.createRequest, name='create'),
    url(r'^success/$', views.createSuccess, name='createSuccess'),
    url(r'^search/$', views.search, name='search'),
)