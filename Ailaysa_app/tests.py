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
        # create sample Publisher
        self.publisher1 = Publisher.objects.create(name='publisher1', address='chennai', country='india')
        self.publisher2 = Publisher.objects.create(name='publisher2', address='chennai', country='india')
        self.publisher3 = Publisher.objects.create(name='publisher3', address='chennai', country='india')

        # create sample user
        self.user = User.objects.create_user(
            name='test_user',
            email='testuser@gmail.com',
            password='1234@abcd',
            publisher=self.publisher1
        )
        user_data = {
            'email': 'testuser@gmail.com',
            'password': '1234@abcd',
        }
        response = self.client.post(reverse('login'), user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.access_token = response.data['access']

        # create sample language
        self.language1 = Language.objects.create(language='language1')
        self.language2 = Language.objects.create(language='language2')
        self.language3 = Language.objects.create(language='language3')

        # create sample genre
        self.genre1 = Genre.objects.create(genre='genre1')
        self.genre2 = Genre.objects.create(genre='genre2')
        self.genre3 = Genre.objects.create(genre='genre3')

        # create sample author
        self.author1 = Author.objects.create(name='author1', about='author_bio1')
        self.author2 = Author.objects.create(name='author2', about='author_bio2')
        self.author3 = Author.objects.create(name='author3', about='author_bio3')

        # create sample book data in the database
        self.book1 = Book.objects.create(
            title='book1',
            author=self.author1,
            publisher=self.publisher1,
            language=self.language1,
            genre=self.genre1,
            isbn10='1401575141',
            isbn13='978-1401575141',
            date_of_publication='1990-07-01',
            number_of_pages='200',
            summary_of_book='summary1',
            keywords='keyword1',
            format='Ebook',
            price='200'
        )

        self.book2 = Book.objects.create(
            title='book2',
            author=self.author2,
            publisher=self.publisher2,
            language=self.language2,
            genre=self.genre2,
            isbn10='1401575142',
            isbn13='978-1401575142',
            date_of_publication='1990-07-02',
            number_of_pages='200',
            summary_of_book='summary2',
            keywords='keyword2',
            format='Ebook',
            price='200'
        )

    def test_book_get_list(self):
        """
        Test book GET list endpoint
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)      # checking the status code

        books = Book.objects.filter(publisher=self.user.publisher)      # get data from the database
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)        # checking the data

    def test_book_get_list_unauthorised(self):
        """
        Test book GET list endpoint without the token
        """
        response = self.client.get(reverse('book-list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)      # checking the status code

    def test_book_get_detail_valid(self):
        """
        Test book GET detail endpoint
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)      # checking the status code

        book = Book.objects.get(pk=self.book1.pk)      # get data from the database
        serializer = BookSerializer(book)
        self.assertEqual(response.data, serializer.data)        # checking the data

    def test_book_get_detail_invalid(self):
        """
        test book GET detail endpoint while the book does not exist
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(reverse('book-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_book_get_detail_unauthorised(self):
        """
        Test book GET detail endpoint without token
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book2.pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)      # checking the status code

    def test_book_post_valid(self):
        """
        Test book POST (create) endpoint
        """
        valid_data = {
            'title': 'book3',
            'author': self.author3.pk,
            'publisher': self.publisher1.pk,       # publisher1 --> user1
            'language': self.language3.pk,
            'genre': self.genre3.pk,
            'isbn10': '1401575143',
            'isbn13': '978-1401575143',
            'date_of_publication': '1990-07-03',
            'number_of_pages': '200',
            'summary_of_book': 'summary3',
            'keywords': 'keyword3',
            'format': 'Ebook',
            'price': '200'
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(reverse('book-list'), valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)     # checking the status code

        book = Book.objects.get(title='book3')
        serializer = BookSerializer(book)
        self.assertEqual(response.data, serializer.data)        # checking the data

    def test_book_post_invalid(self):
        """
        test book post (create) endpoint for invalid data
        """
        invalid_data = {
            'title': '',
            'author': self.author3.pk,
            'publisher': self.publisher1.pk,
            'language': self.language3.pk,
            'genre': self.genre3.pk,
            'isbn10': '1401575143',
            'isbn13': '978-1401575143',
            'date_of_publication': '1990-07-03',
            'number_of_pages': '200',
            'summary_of_book': 'summary4',
            'keywords': 'keyword4',
            'format': 'Ebook',
            'price': '200'
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(reverse('book-list'), invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_book_post_unauthorised(self):
        """
        Test book POST (create) endpoint without token
        """
        valid_data = {
            'title': 'book4',
            'author': self.author3.pk,
            'publisher': self.publisher3.pk,       # publisher3 --> not linked with user1
            'language': self.language3.pk,
            'genre': self.genre3.pk,
            'isbn10': '1401575143',
            'isbn13': '978-1401575143',
            'date_of_publication': '1990-07-04',
            'number_of_pages': '200',
            'summary_of_book': 'summary4',
            'keywords': 'keyword4',
            'format': 'Ebook',
            'price': '200'
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer ')
        response = self.client.post(reverse('book-list'), valid_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)     # checking the status code

    def test_book_put_valid(self):
        """
        Test book PUT (update) endpoint
        """
        valid_data = {
            'title': 'book1',
            'author': self.author3.pk,
            'publisher': self.publisher1.pk,       # publisher1 --> user1
            'language': self.language3.pk,
            'genre': self.genre3.pk,
            'isbn10': '1401575143',
            'isbn13': '978-1401575143',
            'date_of_publication': '1990-07-03',
            'number_of_pages': '200',
            'summary_of_book': 'summary5',
            'keywords': 'keyword3',
            'format': 'Ebook',
            'price': '200'
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book1.pk}), valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)     # checking the status code

        book = Book.objects.get(title='book3')
        serializer = BookSerializer(book)
        self.assertEqual(response.data, serializer.data)        # checking the data

    def test_book_put_invalid(self):
        """
        test book put (update) endpoint for invalid data
        """
        invalid_data = {
            'title': '',
            'author': self.author3.pk,
            'publisher': self.publisher1.pk,
            'language': self.language3.pk,
            'genre': self.genre3.pk,
            'isbn10': '1401575143',
            'isbn13': '978-1401575143',
            'date_of_publication': '1990-07-03',
            'number_of_pages': '200',
            'summary_of_book': 'summary4',
            'keywords': 'keyword4',
            'format': 'Ebook',
            'price': '200'
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book1.pk}), invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_book_put_unauthorised(self):
        """
        Test book PUT (Update) endpoint  without token
        """
        valid_data = {
            'title': 'book2',
            'author': self.author3.pk,
            'publisher': self.publisher3.pk,
            'language': self.language3.pk,
            'genre': self.genre3.pk,
            'isbn10': '1401575143',
            'isbn13': '978-1401575143',
            'date_of_publication': '1990-07-04',
            'number_of_pages': '200',
            'summary_of_book': 'summary4',
            'keywords': 'keyword4',
            'format': 'Ebook',
            'price': '200'
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book2.pk}), valid_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)     # checking the status code

    def test_book_delete_valid(self):
        """
        Test DELETE endpoint for valid data
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_book_delete_invalid(self):
        """
        Test DELETE endpoint for invalid data
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.delete(reverse('book-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_book_delete_unauthorised(self):
        """
        Test DELETE endpoint for valid data
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book2.pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
