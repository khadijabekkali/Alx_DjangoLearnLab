from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create users
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        self.client = APIClient()

        # Create sample books
        self.book1 = Book.objects.create(
            title="Python Basics",
            author="John Doe",
            publication_year=2020
        )

        self.book2 = Book.objects.create(
            title="Advanced Django",
            author="Jane Smith",
            publication_year=2022
        )

        # Endpoints
        self.list_url = reverse("book-list")
        self.detail_url = reverse("book-detail", args=[self.book1.id])

    # -----------------------------
    # READ TESTS
    # -----------------------------
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # -----------------------------
    # CREATE TEST
    # -----------------------------
    def test_create_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")

        data = {
            "title": "New Book",
            "author": "New Author",
            "publication_year": 2024
        }

        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Unauthorized Book",
            "author": "No User",
            "publication_year": 2024
        }

        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # -----------------------------
    # UPDATE TEST
    # -----------------------------
    def test_update_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")

        data = {
            "title": "Updated Title",
            "author": "John Doe",
            "publication_year": 2021
        }

        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    # -----------------------------
    # DELETE TEST
    # -----------------------------
    def test_delete_book_authenticated(self):
        self.client.login(username="testuser", password="testpass123")

        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # -----------------------------
    # FILTERING TEST
    # -----------------------------
    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + "?author=John Doe")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # -----------------------------
    # SEARCH TEST
    # -----------------------------
    def test_search_books(self):
        response = self.client.get(self.list_url + "?search=Python")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    # -----------------------------
    # ORDERING TEST
    # -----------------------------
    def test_order_books_by_year(self):
        response = self.client.get(self.list_url + "?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["publication_year"], 2020)
