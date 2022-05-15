"""studdybuddy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from chat import views as chat_views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', include(('chat.urls', 'chat'), namespace='chat')),
    #path(),
    # path("", include("matching.urls")), # now http://127.0.0.1:8000/ will also take the urls created in matching
    path('pairs/', include('pairs.urls')),
    path('admin/', admin.site.urls),
    path("dashboard/", views.dashboard_view, name="dashboard"), # this is where people can see their dashboard - ex: what their classes are, their messages, their friends, etc.
    # path('login/', views.login, name="login"), # going to http://127.0.0.1:8000/login/ will direct you to a page that says you're logged in 
    # path('login/', TemplateView.as_view(template_name="index.html"), name="index"), 
    path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/', include('allauth.urls')),
    path('home/', views.logout_view, name="logout"),
    path('edit_profile/', views.edit_profile_view, name="edit_profile"), 
    path('view_profile/', views.profile_view, name='view_profile'), # HERE 
    path('create_profile/', views.create_profile_view, name='create_profile'),
    path('edit_classes/', views.edit_classes_view, name="edit_classes"),
    path('code_of_conduct/', views.code_of_conduct_view, name='code_of_conduct'),
    path('about/', views.about_view, name='about'),
    path("profile_list/", views.profile_list, name="profile_list"), # this is where people can see other people's profiles for their specified class
    path("profile/<int:pk>", views.matchingprofile, name="matchingprofile"), # this is where people can see their profile and hopefully have the option to edit 
    path('forum/', views.forum, name='forum'),
    path('forum/<str:room>/', views.room, name='room'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
    path('createsession/', views.create_study_session, name='createstudysession'),
    path('sessions/', views.sessions_view, name='sessions'),
]
