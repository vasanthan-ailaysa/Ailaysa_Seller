from django.db import models
from django.contrib.auth.models import AbstractUser
from seller_auth.Managers import UserManager


class SellerUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('Publisher', 'Publisher'),
        ('Author', 'Author'),
    )

    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    username = None
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def is_publisher(self):
        return self.user_type == 'Publisher'

    def is_author(self):
        return self.user_type == 'Author'

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name
