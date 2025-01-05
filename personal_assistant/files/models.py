# files/models.py

from django.db import models

# Модель для зберігання інформації про файли користувачів
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')  # Поле для файлу
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
    
    # Категорія файлу
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Дата завантаження
    file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.file.name
