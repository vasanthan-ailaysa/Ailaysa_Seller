from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from Ailaysa_app.models import Book, Genre, Language, Format
from Ailaysa_app.serializers import BookSerializer
from seller_auth.models import User


class BookListTestCase(APITestCase):
    """
    TO test GET List endpoint of the Book API
    """

    def setUp(self):
        """
        setup function to create the user and login
        create sample data
        """

        # create sample user and storing the access token
        self.user = User.objects.create_user(
            name='test_user',
            email='testuser@gmail.com',
            password='1234@abcd',
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

        # create sample formate
        self.format1 = Genre.objects.create(format='format1')
        self.format2 = Genre.objects.create(format='format2')
        self.format3 = Genre.objects.create(format='format3')

        # create sample book data in the database
        self.book1 = Book.objects.create(
            title='book1',
            author='author1',
            publisher='publisher1',
            language=self.language1,
            genre=self.genre1,
            isbn10='1401575141',
            isbn13='978-1401575141',
            date_of_publication='1990-07-01',
            number_of_pages='200',
            summary_of_book='summary1',
            keywords='keyword1',
            format=self.format1,
            price='200'
        )

        self.book2 = Book.objects.create(
            title='book2',
            author='author2',
            publisher='publisher2',
            language=self.language2,
            genre=self.genre2,
            isbn10='1401575142',
            isbn13='978-1401575142',
            date_of_publication='1990-07-02',
            number_of_pages='200',
            summary_of_book='summary2',
            keywords='keyword2',
            format=self.format2,
            price='200'
        )

        self.valid_data = {
            'title': 'book3',
            'author': 'author3',
            'publisher': 'publisher1',
            'language': self.language3.pk,
            'genre': self.genre3.pk,
            'isbn10': '1401575143',
            'isbn13': '978-1401575143',
            'date_of_publication': '1990-07-03',
            'number_of_pages': '200',
            'summary_of_book': 'summary3',
            'keywords': 'keyword3',
            'format': self.format3,
            'price': '200'
        }

        self.invalid_data = {
            'title': '',
            'author': 'author3',
            'publisher': 'publisher1',
            'language': self.language3.pk,
            'genre': self.genre3.pk,
            'isbn10': '1401575143128489',
            'isbn13': '978-14015751439823849',
            'date_of_publication': '1990-07-03',
            'number_of_pages': '200',
            'summary_of_book': 'summary3',
            'keywords': 'keyword3',
            'format': self.format3,
            'price': '200'
        }

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
        Test book GET detail endpoint for invalid data
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(reverse('book-detail', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_book_get_detail_unauthorised(self):
        """
        Test book GET detail endpoint for invalid token
        """
        response = self.client.get(reverse('book-detail', kwargs={'pk': self.book1.pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)      # checking the status code

    def test_book_post_valid(self):
        """
        Test book POST endpoint for valid data
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(reverse('book-list'), self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)     # checking the status code

        book = Book.objects.get(title='book3')
        serializer = BookSerializer(book)
        self.assertEqual(response.data, serializer.data)        # checking the data

    def test_book_post_invalid(self):
        """
        Test book post endpoint for invalid data
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(reverse('book-list'), self.invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_book_post_unauthorised(self):
        """
        Test book POST endpoint for invalid token
        """
        response = self.client.post(reverse('book-list'), self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)     # checking the status code

    def test_book_put_valid(self):
        """
        Test book PUT endpoint for valid data
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book2.pk}), self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED) # todo status code     # checking the status code

        book = Book.objects.get(title='book3')
        serializer = BookSerializer(book)
        self.assertEqual(response.data, serializer.data)        # checking the data

    def test_book_put_invalid(self):
        """
        Test book PUT endpoint for invalid data
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book2.pk}), self.invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_book_put_unauthorised(self):
        """
        Test book PUT endpoint for invalid token
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book2.pk}), self.valid_data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)     # checking the status code

    def test_book_delete_valid(self):
        """
        Test Book DELETE endpoint for valid data
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book2.pk}))
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
        Test DELETE endpoint for invalid token
        """
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book2.pk}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
