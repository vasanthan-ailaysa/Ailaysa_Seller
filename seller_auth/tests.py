from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from seller_auth.models import User
from seller_auth.serializers import UserSerializer
from Ailaysa_app.models import Publisher


class ResisterTestCase(APITestCase):
    """
    To test registration endpoint
    """

    def setUp(self):
        """
        setup function to create publisher
        """
        self.publisher = Publisher.objects.create(
            name='publisher1',
            address='chennai',
            country='India'
        )

    def test_register_valid(self):
        """
        test register endpoint for valid data
        """
        register_data = {
            'name': 'user1',
            'email': 'user1@gmail.com',
            'password': '1234@abcd',
            'publisher': self.publisher.pk,
        }

        response = self.client.post(reverse('sign_up'), register_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(name='user1')
        serializer = UserSerializer(user)
        self.assertEqual(response.data, serializer.data)

    def test_register_invalid(self):
        """
        test register endpoint for invalid data
        """
        register_data = {
            'name': 'user2',
            'email': 'user2gmail.com',
            'password': '1234@abcd',
            'publisher': '1'
        }

        response = self.client.post(reverse('sign_up'), register_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginTestCase(APITestCase):
    """
    To test the login endpoint
    """

    def setUp(self):
        """
        setup function to create the user
        """
        self.user = User.objects.create_user(
            name='test_user',
            email='testuser@gmail.com',
            password='1234@abcd'
        )

    def test_login_valid(self):
        """
        test login for valid data
        """
        login_data = {
            'email': 'testuser@gmail.com',
            'password': '1234@abcd',
        }

        response = self.client.post(reverse('login'), login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_invalid(self):
        """
        test login for invalid data
        """
        login_data = {
            'email': 'testuser@gmail.com',
            'password': '1234@abcd23',
        }

        response = self.client.post(reverse('login'), login_data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class LogoutTestCase(APITestCase):
    """
    To test logout endpoint
    """

    def setUp(self):
        """
        setup function to create the user and login
        """
        self.user = User.objects.create_user(
            name='test_user',
            email='testuser@gmail.com',
            password='1234@abcd'
        )
        login_data = {
            'email': 'testuser@gmail.com',
            'password': '1234@abcd',
        }
        response = self.client.post(reverse('login'), login_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.refresh_token = response.data['refresh']
        self.access_token = response.data['access']

    def test_logout_valid(self):
        """
        test logout endpoint for valid token
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(reverse('logout'), {'refresh_token': f'{self.refresh_token}'})
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)

    def test_logout_invalid(self):
        """
        test logout endpoint for invalid token
        """
        self.refresh_token = 12345
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(reverse('logout'), {'refresh_token': f'{self.refresh_token}'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
