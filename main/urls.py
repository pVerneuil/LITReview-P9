from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("my_posts", views.my_posts, name="my_posts"),
    path("create_ticket", views.create_ticket, name="create_ticket"),
    path("create_review", views.create_review, name="create_review"),
    path("response_ticket/<ticket_id>", views.response_ticket, name="response_ticket"),
]
