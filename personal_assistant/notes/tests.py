from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Note, Tag


class TestNoteViews(TestCase):
    databases = {"default"}

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testuser", password="12345")

    def setUp(self):
        self.client = Client()
        self.client.login(username="testuser", password="12345")
        self.note = Note.objects.create(
            user_id=self.user.id, title="Test Note", content="Test Content"
        )
        self.tag = Tag.objects.create(name="Test Tag")
        self.note.tags.add(self.tag)

    def test_note_list_search(self):
        # Test search by title
        response = self.client.get(reverse("notes:note_list") + "?q=Test")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.note, response.context["notes"])

        # Test search by content
        response = self.client.get(reverse("notes:note_list") + "?q=Content")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.note, response.context["notes"])

        # Test search with no results
        response = self.client.get(reverse("notes:note_list") + "?q=NonExistent")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["notes"]), 0)

    def test_note_list_tag_filter(self):
        # Test filtering by tag
        response = self.client.get(reverse("notes:note_list") + f"?tag={self.tag.id}")
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.note, response.context["notes"])

        # Test filtering by non-existent tag
        response = self.client.get(reverse("notes:note_list") + "?tag=999")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context["notes"]), 0)

    def test_tag_create(self):
        # Test tag creation
        response = self.client.post(reverse("notes:tag_create"), {"name": "New Tag"})
        self.assertRedirects(response, reverse("notes:note_list"))
        self.assertTrue(Tag.objects.filter(name="New Tag").exists())

        # Test empty tag name
        initial_count = Tag.objects.count()
        response = self.client.post(reverse("notes:tag_create"), {"name": ""})
        self.assertRedirects(response, reverse("notes:note_list"))
        self.assertEqual(Tag.objects.count(), initial_count)

    # Update existing tests with correct redirect paths
    def test_note_delete_view(self):
        response = self.client.get(
            reverse("notes:note_delete", kwargs={"pk": self.note.pk})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "notes/note_confirm_delete.html")

        response = self.client.post(
            reverse("notes:note_delete", kwargs={"pk": self.note.pk})
        )
        self.assertRedirects(response, reverse("notes:note_list"))
        self.assertEqual(Note.objects.filter(pk=self.note.pk).count(), 0)

    def test_note_toggle_done(self):
        self.assertFalse(self.note.done)

        response = self.client.post(
            reverse("notes:note_toggle_done", kwargs={"pk": self.note.pk})
        )
        self.assertRedirects(response, reverse("notes:note_list"))

        updated_note = Note.objects.get(pk=self.note.pk)
        self.assertTrue(updated_note.done)

    @classmethod
    def tearDown(cls):
        Note.objects.all().delete()
        Tag.objects.all().delete()
        User.objects.all().delete()