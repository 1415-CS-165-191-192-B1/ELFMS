from django.contrib import admin
from django.conf.urls import patterns, include, url
# from login.views import HelloTemplate
# import login views itong nasa baba 
from login import views
#from ELFMS import views
from login.forms import ContactForm1, ContactForm2, ContactForm3
from login.views import ContactWizard
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ELFMS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),

    #default home view
    #url(r'', views.login),
    # how to normal call
	# url(r'^hello/$', views.hello, name='hello'),
	# url(r'^hello_template/$', views.hello_template, name='hello_template'),
	# calling urls for a class
	# url(r'^hello_template_simple/$', views.hello_template_simple, name='hello_template_simple'),
	# url(r'^hello_class/$', HelloTemplate.as_view(), name='hello_class'),

	#getting an id
	#url(r'^get/(?P<article_id>\d+)/$'), articles.views.artivle'),
	#user auth urls
	url(r'^accounts/login/$', views.login),
	url(r'^accounts/auth/$', views.auth_view),
	url(r'^accounts/logout/$', views.logout),
	
	url(r'^accounts/loggedin/$', views.loggedin),
	url(r'^accounts/invalid/$', views.invalid_login),
	url(r'^accounts/register/$', views.register_user),
	url(r'^accounts/register_success/$', views.register_success),
    url(r'^contact/$', ContactWizard.as_view([ContactForm1, ContactForm2, ContactForm3])),
#    url(r'^search/', include('haystack.urls')),

)


