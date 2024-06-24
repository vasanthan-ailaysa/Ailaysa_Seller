from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from seller_auth.models import SellerUser


class ResisterTestCase(APITestCase):
    """
    To test registration endpoint
    """

    def test_register(self):
        url = reverse('sign_up')
        data = {
            "name": "user2",
            "email": "user2@gmail.com",
            "password": "dsahskdjfhdkjf"
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class LoginLogoutTestCase(APITestCase):
    """
    To test the login logout of the user
    """
    refresh_token = ''
    access_token = ''

    def setUp(self):
        """
        function to create the user
        """
        self.user = SellerUser.objects.create_user(
            name="testcaseuser",
            email="testcaseuser@gmail.com",
            password="1234@abcd"
        )


    def test_login(self):
        data = {
            'email': 'testcaseuser@gmail.com',
            'password': '1234@abcd',
        }
        url = reverse('login')
        response = self.client.post(url, data, follow=True)
        self.refresh_token = response.data["refresh_token"]
        self.access_token = response.data["access_token"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # TODO test logout
    def test_logout(self):
        url = reverse('logout')
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + str(self.access_token))
        response = self.client.post(url, {"refresh_token": str(self.refresh_token)})
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
