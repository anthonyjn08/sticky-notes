from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Note


class NoteModelTest(TestCase):
    """
    Unit tests for the Note model.

    These tests validate that Note objects are created correctly
    and that their fields contain the expected data.
    """
    def setUp(self):
        """
        Create a test user and a Note object to use in the tests.
        """
        # Create a test user
        user = User.objects.create_user(
            username="testuser",
            password="hyperion123",
            email="testuser@test.com"
        )

        # Create a Note object for testing
        Note.objects.create(
            user=user,
            title="Test Note",
            content="This is a test note.",
            priority=2,
        )

    def test_note_has_title(self):
        """
        Ensure the Note object has the correct title.
        """
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, "Test Note")

    def test_note_has_content(self):
        """
        Ensure the Note object has the correct content.
        """
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, "This is a test note.")


class NoteViewTest(TestCase):
    """
    Unit tests for Note-related views.

    These tests check that core views like note_list and note_detail
    return the expected responses and display the correct content.
    """
    def setUp(self):
        """
        Create a test user and Note object for view testing.
        """
        # Create a test user
        user = User.objects.create_user(
            username="testuser",
            password="hyperion123",
            email="testuser@test.com"
        )

        # Create a Note object for testing
        Note.objects.create(
            user=user,
            title="Test Note",
            content="This is a test note.",
            priority=2,
        )

        # Log in the test client
        self.client.login(username="testuser", password="hyperion123")

    def test_note_list(self):
        """
        Test that the note_list view returns status 200
        and contains the created Note's title.
        """
        response = self.client.get(reverse("note_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")

    def test_note_detail_view(self):
        """
        Test that the note_detail view returns status 200
        for a valid Note and displays its content.
        """
        note = Note.objects.get(id=1)
        response = self.client.get(reverse("note_detail",
                                           args=[str(note.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Note")
        self.assertContains(response, "This is a test note.")
