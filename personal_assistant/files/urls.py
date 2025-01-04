from django.urls import path
from files import views

app_name = "files"

urlpatterns = [
    path("upload/", views.upload_file, name="upload_file"),
    path("file_list/", views.file_list, name="file_list"),
]