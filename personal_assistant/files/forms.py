"""This module contains the form for uploading files."""

from django import forms
from files.models import File


class FileUploadForm(forms.ModelForm):
    """Class FileUploadForm representing a person"""

    class Meta:
        """Class Meta representing a person"""

        model = File
        fields = ["name", "file", "category"]
