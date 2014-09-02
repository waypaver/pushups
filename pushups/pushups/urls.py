from django.conf.urls import patterns, include, url
from django.contrib import admin
from pushups import views
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.test_index, name='test_index'),
	url(r'^admin/', include(admin.site.urls)),
)
