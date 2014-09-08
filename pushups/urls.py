from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pushups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='test_index'),
    url(r'^admin/', include(admin.site.urls)),

<<<<<<< HEAD
=======
    (r'^accounts/', include('userprofile.urls')),

>>>>>>> youser
    #user auth urls
    url(r'^accounts/login/$', 'main.views.login'),
    url(r'^accounts/auth/$', 'main.views.auth_view'),
    url(r'^accounts/logout/$', 'main.views.logout'),
    url(r'^accounts/loggedin/$', 'main.views.loggedin'),
    url(r'^accounts/invalid/$', 'main.views.invalid_login'),

    #registration urls
    url(r'^accounts/register/$', 'main.views.register_user', name='register'),
    url(r'^accounts/register_success/$', 'main.views.register_success'),
    url(r'^sms/$', views.sms),
)
