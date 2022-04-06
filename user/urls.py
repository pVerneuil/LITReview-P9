from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_user, name="login"),
    path("logout_user", views.logout_user, name="logout"),
    path("register_user", views.register_user, name="register_user"),
    path("follows", views.follows, name="follows"),
    path("unfollow/<follow_id>", views.unfollow, name="unfollow"),
]
