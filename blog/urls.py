__author__ = 'oleksandr'
from django.conf.urls import patterns, url
from blog import views

urlpatterns=patterns('',
                     url(r'^$', views.index, name='index'),
                     url(r'^register$', views.register, name='register'),
                     url(r'^login$', views.auth_login, name='login'),
                     url(r'^logout$', views.auth_logout, name='logout'),
)
