"""Module providing a function printing python version."""

from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('image', 'Image'),
    ('document', 'Document'),
    ('video', 'Video'),
    ('other', 'Other'),
]

class File(models.Model):
    """Class File representing a person"""
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
        """__str__ returns <type 'str'>"""
        self.title = self.name
        return self.name
