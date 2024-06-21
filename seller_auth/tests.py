from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from seller_auth.models import SellerUser


class ResisterTestCase(APITestCase):
    """
    To test registration endpoint
    """

    def test_register(self,):
        url = reverse('sign_up')
        data = {
            'name': 'AAA',
            'email': 'aaa@gmail.com',
            'password': 'abcd1234'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SellerUser.objects.count(), 1)
        self.assertEqual(SellerUser.objects.get().name, 'AAA')