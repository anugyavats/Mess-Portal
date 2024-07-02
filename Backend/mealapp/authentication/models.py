# authentication/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    rollno = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.username
