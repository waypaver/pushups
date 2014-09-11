from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import views
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pushups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$', views.index, name='test_index'),
    url(r'^admin/', include(admin.site.urls)),

    #(r'^accounts/', include('userprofile.urls')),
    #user auth urls
    #url(r'^accounts/login/$', 'main.views.login'),
    #url(r'^accounts/auth/$', 'main.views.auth_view'),
    #url(r'^accounts/logout/$', 'main.views.logout'),
    #url(r'^accounts/loggedin/$', 'main.views.loggedin'),
    #url(r'^accounts/invalid/$', 'main.views.invalid_login'),

    #registration urls
    #url(r'^accounts/register/$', 'main.views.register_user', name='register'),
    #url(r'^accounts/register_success/$', 'main.views.register_success'),
    url(r'^sms/$', views.sms),

    url(r'^$',TemplateView.as_view(template_name='index.html'),name='index'),

    url(r'^accounts/',
        include('registration.backends.simple.urls')),

    url(r'^accounts/profile/',
        TemplateView.as_view(template_name='profile.html'),
        name='profile'),

    url(r'^login/',
        'django.contrib.auth.views.login',
        name='login')
)
