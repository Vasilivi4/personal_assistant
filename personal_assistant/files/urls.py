"""Module providing a function printing python version."""

from django.urls import path
from files import views

app_name = "files"

urlpatterns = [
    path('files/', views.file_list, name='file_list'),
    path('upload/', views.file_upload, name='file_upload'),
]
