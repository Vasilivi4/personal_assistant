import pytest
from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Note, Tag


class TestNoteViews(TestCase):
    def setUp(self):
        # Create test user
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', 
            password='12345'
        )
        self.client.login(username='testuser', password='12345')

        # Create test note
        self.note = Note.objects.create(
            user_id=self.user.id,
            title="Test Note",
            content="Test Content"
        )

        # Create test tag
        self.tag = Tag.objects.create(name="Test Tag")
        self.note.tags.add(self.tag)

    def test_note_delete_view(self):
        # Test GET request
        response = self.client.get(
            reverse('notes:note_delete', kwargs={'pk': self.note.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_confirm_delete.html')

        # Test POST request (actual deletion)
        response = self.client.post(
            reverse('notes:note_delete', kwargs={'pk': self.note.pk})
        )
        self.assertRedirects(response, reverse('notes:note_list'))
        self.assertEqual(Note.objects.filter(pk=self.note.pk).count(), 0)

    def test_note_delete_unauthorized(self):
        # Create another user
        other_user = User.objects.create_user(
            username='otheruser', 
            password='12345'
        )
        # Create note for other user
        other_note = Note.objects.create(
            user_id=other_user.id,
            title="Other's Note",
            content="Private Content"
        )

        # Try to delete other user's note
        response = self.client.post(
            reverse('notes:note_delete', kwargs={'pk': other_note.pk})
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(Note.objects.filter(pk=other_note.pk).count(), 1)

    def test_note_toggle_done(self):
        # Initial state
        self.assertFalse(self.note.done)

        # Toggle done status
        response = self.client.post(
            reverse('notes:note_toggle_done', kwargs={'pk': self.note.pk})
        )
        self.assertRedirects(response, reverse('notes:note_list'))

        # Verify note is marked as done
        updated_note = Note.objects.get(pk=self.note.pk)
        self.assertTrue(updated_note.done)

        # Toggle again
        response = self.client.post(
            reverse('notes:note_toggle_done', kwargs={'pk': self.note.pk})
        )
        updated_note = Note.objects.get(pk=self.note.pk)
        self.assertFalse(updated_note.done)

    def test_tag_list_view(self):
        # Test tag list view
        response = self.client.get(reverse('notes:tag_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/tag_list.html')
        self.assertIn(self.tag, response.context['tags'])

    def test_tag_list_requires_login(self):
        # Logout user
        self.client.logout()
        
        # Try to access tag list
        response = self.client.get(reverse('notes:tag_list'))
        self.assertEqual(response.status_code, 302)  # Redirects to login
        self.assertIn('login', response.url)

    def tearDown(self):
        # Clean up after tests
        self.note.delete()
        self.tag.delete()
        self.user.delete()