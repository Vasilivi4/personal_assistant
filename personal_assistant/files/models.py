from django.db import models

# Модель для хранения информации о загруженных файлах
class UploadedFile(models.Model):
    CATEGORY_CHOICES = [
        ('image', 'Зображення'),
        ('document', 'Документ'),
        ('video', 'Відео'),
        ('other', 'Інше'),
    ]

    file = models.FileField(upload_to='uploads/')  # Поле для загружаемого файла
    category = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default='other'
    )  # Категория файла
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Дата загрузки

    def __str__(self):
        return self.file.name
