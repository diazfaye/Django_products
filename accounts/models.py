from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Visiteur(AbstractUser):
    address = models.CharField(max_length=120)
    email = models.EmailField()

    def __str__(self):
        return self.username

