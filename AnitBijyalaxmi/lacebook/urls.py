from django.conf.urls import include ,url

from django.contrib import admin

from django.urls import include, path


from . import views

urlpatterns = [

    url(r'^$',views.index),

    url(r'^(?P<lacebook_id>[0-9]+)/$', views.detail),

    ]