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

    def test_language_get_list(self):
        """
        test get list endpoint
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

    def test_genre_get_list(self):
        """
        test genre list endpoint
        """
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

    def test_publisher_get_list(self):
        """
        test publisher get list endpoint
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

    def test_author_get_list(self):
        """
        Test author GET list endpoint
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(reverse('author'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)      # checking the status code

        authors = Author.objects.all()      # get data from the database
        serializer = AuthorSerializer(authors, many=True)
        self.assertEqual(response.data, serializer.data)        # checking the data

    def test_author_get_list_unauthorised(self):
        """
        Test author GET list endpoint without the token
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


class BookTest(APITestCase):
    """
    TO test GET, POST, PUT, DELETE endpoints of the Book API
    """

    def setUp(self):
        """
        setup function to create the user and login
        create sample data
        """
        # create sample user
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

        # create sample Publisher
        self.publisher1 = Publisher.objects.create(name='publisher1', address='chennai', country='india')

        # create sample author
        self.author1 = Author.objects.create(name='author1', about='author_bio')

        # create sample book data in the database
        self.book1 = Book.objects.create(name='author1', about='about1')
        self.book2 = Book.objects.create(name='author2', about='about2')

    def test_book_get_list(self):
        """
        Test book GET list endpoint
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(reverse('book'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)      # checking the status code

        books = Book.objects.all()      # get data from the database
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)        # checking the data

    def test_book_get_list_unauthorised(self):
        """
        Test book GET list endpoint without the token
        """
        response = self.client.get(reverse('book'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)      # checking the status code

    def test_book_get_detail(self):
        """
        Test book GET detail endpoint without the token
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(reverse('book'), kwargs={'pk': self.book1.pk})
        self.assertEqual(response.status_code, status.HTTP_200_OK)      # checking the status code

        book = Book.objects.get(pk=self.book1.pk)      # get data from the database
        serializer = BookSerializer(book, many=True)
        self.assertEqual(response.data, serializer.data)        # checking the data

    def test_book_get_detail_unauthorised(self):
        """
        Test book GET detail endpoint
        """
        response = self.client.get(reverse('book'), kwargs={'pk': self.book1.pk})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)      # checking the status code

    def test_book_post_valid(self):
        """
        Test book POST (create) endpoint
        """
        valid_data = {
            'name': 'book3',
            'about': 'about3'
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(reverse('book'), valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)     # checking the status code

        book = Book.objects.get(name='book3')
        serializer = BookSerializer(book)
        self.assertEqual(response.data, serializer.data)        # checking the data

    def test_book_post_invalid(self):
        """
        test book post (create) endpoint for valid data
        """
        invalid_data = {
            'name': '',
            'about': '',
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(reverse('book'), invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_book_post_unauthorised(self):
        """
        Test book POST (create) endpoint without token
        """
        valid_data = {
            'name': 'author3',
            'about': 'about3'
        }
        response = self.client.post(reverse('book'), valid_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)     # checking the status code
