# coding: utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns('library.views',
    url(r'^$', 'home', name='Home'),
)
