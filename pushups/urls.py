from django.conf.urls import patterns, url
from pushups import views

urlpatterns = patterns('',
    url(r'^', views.test_index, name='test_index'),
    url(r'^test_submit/', views.test_submit, name='test_submit'),
)