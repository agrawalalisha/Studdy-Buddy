from django.urls import include, re_path, path
from . import views

#This re_path is url for Django 4.0+, works with old format
urlpatterns = [
    re_path(r'^$', views.all_rooms, name="all_rooms"),
    re_path(r'token$', views.token, name="token"),
    re_path(r'rooms/(?P<slug>[-\w\d.@%]+)/$', views.room_detail, name="room_detail"),
]