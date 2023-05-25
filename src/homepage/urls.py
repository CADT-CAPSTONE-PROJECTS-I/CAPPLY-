from django.contrib import admin
from django.urls import path
from homepage.views import homepage, register, login, logout, profile,profile_edit, show_category, search
from category import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name="home"),
    path('register/', register, name="register"),
    path("login", login, name="login"),
    path("logout", logout, name="logout"),
    path("profile", profile, name="profile"),
    path("profile_edit", profile_edit, name="profile_edit"),
    path("search", search, name="search"),


    

]