from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from seller_auth.Managers import UserManager
from Ailaysa_app.models import Publisher


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    name = models.CharField(max_length=100, unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name
