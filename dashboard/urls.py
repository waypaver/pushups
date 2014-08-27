from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dashboard.views.home', name='home'),
    #url(r'^pushups/', include('pushups.urls'), namespace='pushups'),
	url(r'^admin/', include(admin.site.urls)),
)
