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
            'name': 'registeruser',
            'email': 'registeruser@gmail.com',
            'password': 'abcd@1234'
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(SellerUser.objects.count(), 1)
        # self.assertEqual(SellerUser.objects.get().name, 'AAA')


class LoginLogoutTestCase(APITestCase):
    """
    To test the login logout of the user
    """

    def SetUp(self):
        """
        function to create the user
        """
        self.user = SellerUser.objects.create_user(
            name='testcaseuser',
            email='testcaseuser@gmail.com',
            password='1234@abcd'
        )

    def test_login(self):
        data = {
            'email': 'testcaseuser@gmail.com',
            'password': '1234@abcd',
        }
        url = reverse('token_obtain_pair')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
