from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pushups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='test_index'),
    url(r'^admin/', include(admin.site.urls)),

)
