from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from twanger.site import views as site_views

urlpatterns = patterns('',
    url(r'^$', site_views.HomeView.as_view(), name='home'),
    url(r'^auth/new/$', site_views.NewUserPostView.as_view(), name='new-user'),
    url(r'^auth/login/$', site_views.LoginPostView.as_view(), name='login'),
    url(r'^auth/logout/$', site_views.LogoutView.as_view(), name='logout'),
    url(r'^auth/new/success/$', site_views.NewUserSuccessView.as_view(),
        name='new-user-success'),

    url(r'^message/', include('twanger.message.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
