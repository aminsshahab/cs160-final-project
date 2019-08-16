# chat/urls.py
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('channel/', views.channel),
    path('connect/', views.connect),
    path('gallery/', views.gallery),
    path('support/', views.support),
    path('channel/index', views.index),
    path('channel/channel', views.channel),
    path('channel/connect', views.connect),
    path('channel/support', views.support),
    path('support/index', views.index),
    path('support/channel', views.channel),
    path('support/support', views.support),
    path('support/connect', views.connect),
    path('support/portrait', views.portrait),
    path('support/solo', views.solo),
    path('support/sent', views.sent),
    path('connect/support', views.support),
    path('connect/channel', views.channel),
    path('connect/connect', views.connect),
    path('connect/portrait', views.portrait),
    path('connect/sent', views.sent),
    path('connect/solo', views.solo),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]

