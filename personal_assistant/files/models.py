from storages.backends.gcloud import GoogleCloudStorage
from django.db import models


class UserFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    category = models.CharField(
        max_length=10,
        choices=[
            ('image', 'Зображення'),
            ('document', 'Документ'),
            ('video', 'Відео'),
            ('other', 'Інше'),
        ],
        default='other'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_file_url(self):
        storage = GoogleCloudStorage()
        return storage.url(self.file.name)