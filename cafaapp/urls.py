from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings


from . import views
from . import restful


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cafa/int/login$', views.loginuser, name='login'),
    url(r'^cafa/int/dashboard', views.dash, name='dash'),
    url(r'^cafa/int/new_contract', views.newcontract, name='newcontract'),
    url(r'^cafa/int/view_contract', views.viewcontract, name='viewcontract'),
    url(r'^cafa/ext/login$', views.loginext, name='loginexit'),
    url(r'^cafa/ext/job$', views.job, name='job'),
    url(r'^cafa/ext/jobupdated$', views.jobupdated, name='jobupdated'),
    # API
    url(r'^cafa/api/create_contract$', restful.create_contract, name='create contract'),
    url(r'^cafa/api/get_contracts', restful.get_all_contracts, name='get contract'),
    url(r'^cafa/api/make_job', restful.make_job, name='make job'),
    url(r'^cafa/api/complete_job', restful.complete_job, name='complete job'),
    url(r'^cafa/api/approve_job', restful.approve_job, name='approve job'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
