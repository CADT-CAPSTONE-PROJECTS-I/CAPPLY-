from django.contrib import admin
from django.urls import path, include
from homepage.views import homepage, register, login, logout, profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name="home"),
    path('register/', register, name="register"),
    path("login", login, name="login"),
    path("logout", logout, name="logout"),
    path("profile", profile, name="profile"),

]