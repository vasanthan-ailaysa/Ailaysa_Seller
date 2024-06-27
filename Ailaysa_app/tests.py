from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from Ailaysa_app.models import Book, Genre, Language, Format
from Ailaysa_app.serializers import BookSerializer
from seller_auth.models import User


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
