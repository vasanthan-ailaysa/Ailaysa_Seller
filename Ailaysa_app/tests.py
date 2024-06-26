from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from Ailaysa_app.models import Book, Publisher, Author, Language, Genre
from seller_auth.models import User


# class LanguageTest(APITestCase):
#     """
#     TO test GET endpoint of Language
#     """
#     def test_language_get(self):
#         response = self.client.get(reverse('language'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


# class GenreTest(APITestCase):
#     """
#     TO test GET endpoint of Genre
#     """
#     def test_genre_get(self):
#         response = self.client.get(reverse('genre'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)


class AuthorTest(APITestCase):
    """
    TO test GET endpoint of Author
    """
    token = ''

    def setUp(self):
        self.user = User.objects.create_user(
            name='test_user',
            email='testuser@gmail.com',
            password='123456789@10'
        )

    def test_author_get(self):
        """
        Test author GET endpoint
        """

        # Login and Obtain Token
        login_data = {
            'email': 'testuser@gmail.com',
            'password': '123456789@10'
        }
        response = self.client.post(reverse('login'), login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access']

        # now pass the token and get response
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        response = self.client.get(reverse('author'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
