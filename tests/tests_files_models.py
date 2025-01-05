# tests_files_models.py

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from ..personal_assistant.files.models import UploadedFile

class UploadedFileModelTest(TestCase):
    def test_file_upload(self):
        test_file = SimpleUploadedFile("testfile.txt", b"Test content")
        uploaded_file = UploadedFile.objects.create(file=test_file)
        self.assertEqual(uploaded_file.file.name, "uploads/testfile.txt")

