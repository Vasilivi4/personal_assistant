from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('image', 'Зображення'),
    ('document', 'Документ'),
    ('video', 'Відео'),
    ('other', 'Інше'),
]

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = CloudinaryField('file')
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='other'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
