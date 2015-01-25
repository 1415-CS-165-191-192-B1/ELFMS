from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from twanger.message import views as msg_views

urlpatterns = patterns('',
    url(r'^post/$', msg_views.MessagePostView.as_view(), name='msg-post'),
)
