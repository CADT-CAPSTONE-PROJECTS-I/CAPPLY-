from django.contrib import admin
<<<<<<< HEAD
from django.urls import path
from homepage.views import homepage, register, login, logout, profile, show_category
=======
from django.urls import path, include
from homepage.views import homepage, register, login, logout, profile, profile_edit, show_category

>>>>>>> bc357e2df207a594a8d24c0ebef968fed654675a
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name="home"),
    path('register/', register, name="register"),
    path("login", login, name="login"),
    path("logout", logout, name="logout"),
    path("profile", profile, name="profile"),
    path("profile_edit", profile_edit, name="profile_edit"),
    path("scholarship", show_category, name="scholarship"),

]