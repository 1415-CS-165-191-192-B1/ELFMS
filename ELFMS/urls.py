from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ELFMS.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^request/', include('requestManager.urls', namespace="request")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('login.urls')),
    url(r'^userprofile/', include('userprofile.urls')),
)
admin.autodiscover()
