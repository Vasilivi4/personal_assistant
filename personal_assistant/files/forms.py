# files/forms.py
from django import forms
from .models import UserFile

# Форма для завантаження файлів
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UserFile
        fields = ['file', 'category']  # Поля для файлу та категорії
