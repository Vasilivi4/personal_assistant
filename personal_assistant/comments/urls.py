"""URLs for the comments app."""

from django.urls import path
from comments import views

app_name = "comments"

urlpatterns = [
    path("post/<int:post_id>/comments/", views.comment_list, name="comment_list"),
]
