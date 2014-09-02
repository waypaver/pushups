from django.conf.urls import patterns, include, url
from django.contrib import admin
from pushups import views
from django.contrib.auth.views import login, logout
admin.autodiscover()

urlpatterns = patterns('',
	#url(r'^', views.test_index, name='test_index'),
	url(r'^admin/', include(admin.site.urls)),

  #user auth urls
  url(r'^accounts/login/$', 'pushups.views.login'),
  url(r'^accounts/auth/$', 'pushups.views.auth_view'),
  url(r'^accounts/logout/$', 'pushups.views.logout'),
  url(r'^accounts/loggedin/$', 'pushups.views.loggedin'),
  url(r'^accounts/invalid/$', 'pushups.views.invalid_login'),
)
