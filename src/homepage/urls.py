from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from homepage.views import homepage, register, login, logout, profile, show_category, search
=======
from homepage.views import homepage, register, login, logout, profile,profile_edit, show_category, search
>>>>>>> 0b81603a87c758f8f87a29a79cdf98caa409a436
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
    path("about",name="about"),
    path("contact",name="contact"),


    

]