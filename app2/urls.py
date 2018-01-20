from django.contrib import admin
from django.conf.urls import url

from . import  views
urlpatterns = [
    url('rnd/', views.rnd),
    url('^$', views.main),
    url('stepenRandchisla/(\d*)', views.stepenRandchisla),
    url('MyUsers/', views.MyUsers),
]