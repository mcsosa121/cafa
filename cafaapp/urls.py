from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^int/login$', views.loginuser, name='login'),
    url(r'^int/dashboard', views.dash, name='dash'),
    url(r'^int/new_contract', views.newcontract, name='newcontract'),
    url(r'^int/view_contract', views.viewcontract, name='viewcontract'),
    url(r'^ext/login$', views.loginext, name='loginexit'),
    url(r'^ext/job$', views.job, name='job'),
    url(r'^ext/jobupdated$', views.jobupdated, name='jobupdated'),
]
