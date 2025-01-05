# test_files_forms.py
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from ..personal_assistant.files.forms import UploadFileForm

class UploadFileFormTest(TestCase):
    def test_valid_form(self):
        form_data = {}
        file_data = {'file': SimpleUploadedFile("testfile.txt", b"Test content")}
        form = UploadFileForm(data=form_data, files=file_data)
        self.assertTrue(form.is_valid())

