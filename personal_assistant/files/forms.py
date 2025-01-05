# files/forms.py
from django import forms
from .models import UploadedFile

# Форма для завантаження файлів
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file', 'category']  # Поля для файлу та категорії
