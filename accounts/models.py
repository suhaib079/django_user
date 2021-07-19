from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(('email adress'), unique=True)
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return self.email