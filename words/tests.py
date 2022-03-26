from django.test import TestCase
from django.urls import reverse

from .models import Word

class IndexViewTests(TestCase):

    def test_status_code(self):
        """Checks if the index page returns OK."""
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class FlashCardViewTests(TestCase):

    def test_status_code(self):
        """Checks if the flashcard page returns OK."""
        response = self.client.get(reverse('flashcard'))
        self.assertEqual(response.status_code, 200)


class CategoryApiTests(TestCase):

    def test_status_code(self):
        """Checks if the get_word API returns OK."""
        response = self.client.get(reverse('get_category'))
        self.assertEqual(response.status_code, 200)


class ToipcApiTests(TestCase):

    def test_status_code(self):
        """Checks if the get_topic API returns OK."""
        response = self.client.get(reverse('get_topic'))
        self.assertEqual(response.status_code, 200)


class WordApiTests(TestCase):

    def setUp(self):
        """Populate test database."""
        Word.objects.create(en="hello", jp="konichiwa")

    def test_status_code(self):
        """Checks if the get_word API returns OK."""
        response = self.client.get(reverse('get_word'))
        self.assertEqual(response.status_code, 200)
