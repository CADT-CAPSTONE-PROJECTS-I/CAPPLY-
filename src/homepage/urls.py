from django.contrib import admin
from django.urls import path
from homepage.views import homepage, register, login, logout, profile,profile_edit,contact_us, search, about, contact ,UserDeleteConfirmView
from . import views
# from homepage.views import homepage, register, login, logout, profile,profile_edit, show_category, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homepage, name="home"),
    path('register', register, name="register"),
    path("login", login, name="login"),
    path("logout", logout, name="logout"),
    path("profile", profile, name="profile"),
    path("profile_edit", profile_edit, name="profile_edit"),
    path("search", search, name="search"),
    path("about",about, name="about"),
    path("contact",contact , name="contact"),
    path("contact-us",contact_us , name="contact_us"),
    # path("scholarship_pdf",some_view , name="view_pdf"),
    path('user/delete/', UserDeleteConfirmView.as_view(), name='user_delete_confirm'),
]


