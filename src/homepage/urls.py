from django.urls import path
from homepage.views import homepage, register, login, logout, profile,contact_us, search, about, contact ,UserDeleteView
urlpatterns = [
    path('',homepage, name="home"),
    path('register', register, name="register"),
    path("login", login, name="login"),
    path("logout", logout, name="logout"),
    path("profile", profile, name="profile"),
    path("search", search, name="search"),
    path("about",about, name="about"),
    path("contact",contact , name="contact"),
    path("contact-us",contact_us , name="contact_us"),
    path('user/delete/', UserDeleteView.as_view(), name='user_delete_confirm'),
]


