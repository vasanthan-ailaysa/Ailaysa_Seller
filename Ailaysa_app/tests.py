from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from Ailaysa_app.models import Book, Publisher, Author, Language, Genre
from Ailaysa_app.serializers import BookSerializer, PublisherSerializer, AuthorSerializer, LanguageSerializer, GenreSerializer
from seller_auth.models import User


class LanguageTestCase(APITestCase):
    """
    TO test GET endpoint of Language
    """

    def setUp(self):
        """
        setup function to create sample data
        """

        Language.objects.create(language='Tamil')
        Language.objects.create(language='English')

    def test_language_get_all(self):
        """
        test get all endpoint
        """
        response = self.client.get(reverse('language'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)      # checking the status code

        languages = Language.objects.all()
        serializer = LanguageSerializer(languages, many=True)
        self.assertEqual(response.data, serializer.data)        # checking the data in the database


class GenreTestCase(APITestCase):
    """
    TO test GET endpoint of Genre
    """

    def setUp(self):
        """
        setup function to create sample data
        """
        Genre.objects.create(genre='Biography')
        Genre.objects.create(genre='Fiction')

    def test_genre_get_all(self):
        response = self.client.get(reverse('genre'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)      # checking the status code

        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        self.assertEqual(response.data, serializer.data)  # checking the data in the database


class PublisherTestCase(APITestCase):
    """
    To test GET & POST endpoint of Publisher
    """

    def setUp(self):
        """
        setup function to create sample data
        """
        Publisher.objects.create(name='publisher1', address='chennai', country='India')
        Publisher.objects.create(name='publisher2', address='chennai', country='India')

    def test_publisher_get_all(self):
        """
        test publisher get all (List) endpoint
        """
        response = self.client.get(reverse('publisher'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # checking the status code

        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        self.assertEqual(response.data, serializer.data)  # checking the data in the database

    def test_publisher_post_valid(self):
        """
        test publisher post (create) endpoint for valid data
        """
        valid_data = {
            'name': 'publisher3',
            'address': 'chennai',
            'country': 'India'
        }
        response = self.client.post(reverse('publisher'), valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        publisher = Publisher.objects.get(name='publisher3')
        serializer = PublisherSerializer(publisher)
        self.assertEqual(response.data, serializer.data)

    def test_publisher_post_invalid(self):
        """
        test publisher post (create) endpoint for valid data
        """
        invalid_data = {
            'name': '',
            'address': '',
            'country': ''
        }
        response = self.client.post(reverse('publisher'), invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



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
        user_data = {
            'email': 'testuser@gmail.com',
            'password': '1234@abcd',
        }
        response = self.client.post(reverse('login'), user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.access_token = response.data['access']

        # create sample data in the database
        Author.objects.create(name='author1', about='about1')
        Author.objects.create(name='author2', about='about2')

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

    def test_author_get_all_unauthorised(self):
        """
        Test author GET all endpoint without the token
        """
        response = self.client.get(reverse('author'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)      # checking the status code


    def test_author_post_valid(self):
        """
        Test author POST (create) endpoint
        """
        valid_data = {
            'name': 'author3',
            'about': 'about3'
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(reverse('author'), valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)     # checking the status code

        author = Author.objects.get(name='author3')
        serializer = AuthorSerializer(author)
        self.assertEqual(response.data, serializer.data)        # checking the data

    def test_author_post_invalid(self):
        """
        test author post (create) endpoint for valid data
        """
        invalid_data = {
            'name': '',
            'about': '',
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(reverse('author'), invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_author_post_unauthorised(self):
        """
        Test author POST (create) endpoint without token
        """
        valid_data = {
            'name': 'author3',
            'about': 'about3'
        }
        response = self.client.post(reverse('author'), valid_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)     # checking the status code


