from django.urls import path
from . import views

urlpatterns = [
    path("", views.feed, name="home"),
    path("home", views.feed, name="home"),
    path("my_posts", views.see_my_posts, name="my_posts"),
    path("create_ticket", views.create_ticket, name="create_ticket"),
    path("create_review", views.create_review, name="create_review"),
    path("response_ticket/<ticket_id>", views.response_ticket, name="response_ticket"),
    path(
        "delete_content/<content_type>/<content_id>",
        views.delete_content,
        name="delete_content",
    ),
    path("update_ticket/<ticket_id>", views.update_ticket, name="update_ticket"),
    path("update_review/<review_id>", views.update_review, name="update_review"),
]
