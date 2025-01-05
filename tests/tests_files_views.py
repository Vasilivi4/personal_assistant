# tests_files_views.py

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from ..personal_assistant.files.models import UploadedFile

# тест files/views.py/class upload_file
class FileUploadViewTest(TestCase):
    def test_upload_file_valid(self):
        
        # Тест завантаження валідного файлу
        url = reverse('upload_file')  # URL уявлення для завантаження файлу
        file_data = {
            'file': SimpleUploadedFile("testfile.txt", b"Test content"),
            'category': 'documents'
        }
        response = self.client.post(url, file_data)
        self.assertEqual(response.status_code, 302)  # Очікуємо перенаправлення
        self.assertEqual(UploadedFile.objects.count(), 1)  # Перевіряємо, що файл збережений у базі даних
        uploaded_file = UploadedFile.objects.first()
        self.assertEqual(uploaded_file.file.name, "uploads/testfile.txt")
        self.assertEqual(uploaded_file.category, "documents")

    def test_upload_file_invalid(self):
        
        # Тест завантаження без файлу
        url = reverse('upload_file')
        file_data = {'category': 'documents'}  # Без файлу
        response = self.client.post(url, file_data)
        self.assertEqual(response.status_code, 200)  # Сторінка має залишитися
        self.assertContains(response, "This field is required.")  # Перевіряємо повідомлення про помилку

# тест files/views.py/class file_list
class FileListViewTest(TestCase):
    def setUp(self):

        # Налаштування тестових даних.
        UploadedFile.objects.create(file="uploads/image1.jpg", category="images")
        UploadedFile.objects.create(file="uploads/doc1.pdf", category="documents")
        UploadedFile.objects.create(file="uploads/video1.mp4", category="videos")

    def test_file_list_all(self):

        # Тест відображення всіх файлів.
        url = reverse('file_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)  # Сторінка доступна
        self.assertContains(response, "image1.jpg")  # Перевіряємо наявність файлу
        self.assertContains(response, "doc1.pdf")
        self.assertContains(response, "video1.mp4")

    def test_file_list_by_category(self):

        # Тест фільтрації за категорією.
        url = reverse('file_list') + '?category=documents'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "doc1.pdf")
        self.assertNotContains(response, "image1.jpg")  # Інші категорії не відображаються
        self.assertNotContains(response, "video1.mp4")

# тест files/views.py порожнього списку
class EmptyFileListViewTest(TestCase):
    def test_empty_file_list(self):
        
        # Тест, коли у базі даних немає файлів
        url = reverse('file_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No files available")  # Припустимо, що така фраза є в шаблоні
