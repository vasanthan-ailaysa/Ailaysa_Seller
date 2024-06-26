from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from Ailaysa_app.models import Book, Publisher, Author, Language, Genre
from Ailaysa_app.serializers import BookSerializer, PublisherSerializer, AuthorSerializer, LanguageSerializer, GenreSerializer
from seller_auth.models import User


class LanguageTest(APITestCase):
    """
    TO test GET endpoint of Language
    """

    def setUp(self):
        """
        setup function to create sample data
        """

        Language.object.create(language='Tamil')
        Language.object.create(language='English')

    def test_language_get_all(self):
        response = self.client.get(reverse('language'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)      # checking the status code

        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        self.assertEqual(response.data, serializer.data)        # checking the data in the databse



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

    def setUp(self):
        """
        setup function to create the user and login
        create sample data
        """
        self.user = User.objects.create_user(
            name='test_user',
            email='testuser@gmail.com',
            password='1234@abcd'
        )
        data = {
            'email': 'testuser@gmail.com',
            'password': '1234@abcd',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.access_token = response.data['access']

        # create sample data
        Author.objects.create(name='author1', about='about1')
        Author.objects.create(name='author2', about='about2')
        Author.objects.create(name='author3', about='about3')

    def test_author_get_all(self):
        """
        Test author GET all endpoint
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(reverse('author'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)      # checking the status code

        authors = Author.objects.all()      # get data from the database
        serializer = AuthorSerializer(authors, many=True)
        self.assertEqual(response.data, serializer.data)        # checking the data

