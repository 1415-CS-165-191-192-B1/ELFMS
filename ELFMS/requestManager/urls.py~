from django.conf.urls import patterns, url

from requestManager import views

urlpatterns = patterns('',
    url(r'^$', views.reqManager, name='request'),
    url(r'^(?P<resource_id>\d+)/$', views.detail, name='detail'),
)

