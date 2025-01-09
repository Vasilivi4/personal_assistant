"""Module providing a function printing python version."""

from django import forms
from files.models import File

class FileUploadForm(forms.ModelForm):
    """Class FilesConfig representing a person"""
    class Meta:
        """Class FilesConfig representing a person"""
        model = File
        fields = ['name', 'file', 'category']

