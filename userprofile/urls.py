from django.conf.urls import patterns, include, url
from userprofile import views
urlpatterns = patterns('',
        url(r'^accounts/profile/$', views.user_profile),
)