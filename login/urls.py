from django.conf.urls import patterns, include, url
from django.contrib import admin
from login import views

urlpatterns = patterns('',

	url(r'^$', views.login),
	url(r'^auth_view/$', views.auth_view),
	url(r'^loggedin/$', views.loggedin),
	url(r'^invalid/$', views.invalid_login),

)