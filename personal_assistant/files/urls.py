# files/urls.py
from storages.backends.gcloud import GoogleCloudStorage
from django.urls import path
from . import views

app_name = 'files'

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),  # Завантаження файлів
    path('files/', views.file_list, name='file_list'),  # Список файлів
    path('files/<str:category>/', views.file_list, name='file_list_by_category'),
]

# URL-адрес для завантажених файлів
storage = GoogleCloudStorage()
file_url = storage.url('<file-path>')

