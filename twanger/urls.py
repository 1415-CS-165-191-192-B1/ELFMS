# From the urls module patterns, include, and url.
# patterns is a wrapper that allows you to prefix all the urls if needed.
# include allows us to include additional urls.py from other apps and namespace
# them.
# and url is a constructor for each RegexURLPattern object.
from django.conf.urls import patterns, include, url

# Include the contrib.admin stuff and run autodiscover to bootstrap it.
from django.contrib import admin
admin.autodiscover()

# Import our main views from twanger/site/views.py
from twanger.site import views as site_views

# The main patterns for our site.
urlpatterns = patterns('',
    # Our home `/` url pattern. We name it `home` using a keyword. This allows
    # us to access it by name in template(tags) without exposing the code.
    url(r'^$', site_views.HomeView.as_view(), name='home'),

    # These are all of our authentication urls. Work exactly as above.
    url(r'^auth/new/$', site_views.NewUserPostView.as_view(), name='new-user'),
    url(r'^auth/new/success/$', site_views.NewUserSuccessView.as_view(),
        name='new-user-success'),
    url(r'^auth/login/$', site_views.LoginPostView.as_view(), name='login'),
    url(r'^auth/logout/$', site_views.LogoutView.as_view(), name='logout'),

    # Here we use the `include` method to load the urls.py from the message
    # app. The `/` url contained in it's urls.py will now be accessed as
    # /message/ and so on for each view it defines.
    url(r'^message/', include('twanger.message.urls')),

    # lastly we include our admin urls. Notice these are an actual module
    # instance not just a string libe the message ones. Either is fine.
    url(r'^admin/', include(admin.site.urls)),
)
