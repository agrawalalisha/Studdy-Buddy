from django.urls import path, include 
from .views import dashboard # deleted profile_list and profile


app_name = "matching"

urlpatterns = [
    # path("", home, name="home"),
    # path("profile_list/", profile_list, name="profile_list"), # this is where people can see other people's profiles for their specified class
    # path("profile/<int:pk>", profile, name="profile"), # this is where people can see their profile and hopefully have the option to edit 
    # info on links can be found at https://realpython.com/django-user-management/
    # http://127.0.0.1:8000/accounts/google/login/ will take you to the google login page 
    # http://127.0.0.1:8000/accounts/login/ will take you to the logged in page 
    # path("profile_creation_view/", profile_creation_view, name="create_profile")
]

