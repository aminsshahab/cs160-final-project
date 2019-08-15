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
<<<<<<< Updated upstream
    path('channel/support', views.support),
=======
>>>>>>> Stashed changes
    path('support/index', views.index),
    path('support/channel', views.channel),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]

