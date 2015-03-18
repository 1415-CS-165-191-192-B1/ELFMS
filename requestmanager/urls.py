from django.conf.urls import patterns, include, url
from requestmanager import views

urlpatterns = patterns('',
	
	# url(r'^accounts/view_request/(?P<requested_id>\d+)/$', views.view_request),
	url(r'^accounts/create_request/$', views.create_request),
	url(r'^accounts/request_success/$', views.request_success),
	#(?P<requested_id>\d+)/
	#url(r'^allaccounts/$', views.view_request),

)