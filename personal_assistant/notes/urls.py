"""Module providing a function printing python version."""

from django.urls import path
from notes import views

app_name = "notes"

urlpatterns = [
    path("notes/", views.note_list, name="note_list"),
    path("create/", views.note_create, name="note_create"),
    path("edit/<int:pk>/", views.note_edit, name="note_edit"),
    path("delete/<int:pk>/", views.note_delete, name="note_delete"),
    path("toggle-done/<int:pk>/", views.note_toggle_done, name="note_toggle_done"),
    path("tag/create/", views.tag_create, name="tag_create"),
]
