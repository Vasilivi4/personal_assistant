from django import forms
from files.models import UploadedFile

# Форма для загрузки файлов
class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file', 'category']  # Поля для файла и категории

