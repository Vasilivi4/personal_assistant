# files/urls.py
from storages.backends.gcloud import GoogleCloudStorage
from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),  # Завантаження файлів
    path('', views.file_list, name='file_list'),  # Список файлів
]

# URL-адрес для завантажених файлів
storage = GoogleCloudStorage()
file_url = storage.url('<file-path>')

