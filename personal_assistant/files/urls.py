# files/urls.py
from storages.backends.gcloud import GoogleCloudStorage
from django.urls import path
from . import views
from google.cloud import storage
from django.conf import settings

app_name = 'files'

urlpatterns = [
    path('upload/', views.upload_file, name='upload_file'),  # Завантаження файлів
    path('files/', views.file_list, name='file_list'),  # Список файлів
    path('files/<str:category>/', views.file_list, name='file_list_by_category'),
]

# URL-адрес для завантажених файлів
storage = GoogleCloudStorage()
file_url = storage.url('<file-path>')

def upload_to_gcs(file, file_name):
    """
    Завантаження файлу на Google Cloud Storage
    """
    # Ініціалізація клієнта
    client = storage.Client.from_service_account_json(settings.GOOGLE_APPLICATION_CREDENTIALS)
    bucket = client.get_bucket(settings.GCS_BUCKET_NAME)

    # Створення об'єкта в bucket
    blob = bucket.blob(file_name)

    # Завантаження файлу
    blob.upload_from_file(file)

    # Доступний URL
    blob.make_public()
    return blob.public_url
