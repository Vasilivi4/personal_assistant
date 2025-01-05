# files/models.py

from django.db import models

# Модель для зберігання інформації про файли користувачів
class UploadedFile(models.Model):
    CATEGORY_CHOICES = [
        ('image', 'Зображення'),
        ('document', 'Документи'),
        ('video', 'Відео'),
        ('other', 'Інше'),
    ]
    
    # збереження файлів
    file = models.FileField(upload_to='uploads/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.category or self.category == 'other':
            file_type = self.file.name.split('.')[-1].lower()
            if file_type in ['jpg', 'jpeg', 'png', 'gif']:
                self.category = 'image'
            elif file_type in ['pdf', 'doc', 'docx', 'txt']:
                self.category = 'document'
            elif file_type in ['mp4', 'avi', 'mkv']:
                self.category = 'video'
            else:
                self.category = 'other'
        super().save(*args, **kwargs)