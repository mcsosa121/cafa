from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


from . import views
from . import restful


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^int/login$', views.loginuser, name='login'),
    url(r'^int/dashboard', views.dash, name='dash'),
    url(r'^int/new_contract', views.newcontract, name='newcontract'),
    url(r'^int/view_contract', views.viewcontract, name='viewcontract'),
    url(r'^ext/login$', views.loginext, name='loginexit'),
    url(r'^ext/job$', views.job, name='job'),
    url(r'^ext/jobupdated$', views.jobupdated, name='jobupdated'),
    # API
    url(r'^api/create_contract$', restful.create_contract, name='create contract'),
    url(r'^api/get_contracts', restful.get_all_contracts, name='get contract'),
    url(r'^api/make_job', restful.make_job, name='make job'),
    url(r'^api/complete_job', restful.complete_job, name='complete job'),
    url(r'^api/approve_job', restful.approve_job, name='approve job'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)