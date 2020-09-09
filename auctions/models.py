from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.conf import settings
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField



class User(AbstractUser):
    pass


class Auction(models.Model):
    author = models.CharField(max_length=50)
    auth = CurrentUserField()
    image = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.FloatField(default=0)

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
        return self.name

class Bids(models.Model):
    number_bids = models.IntegerField


class Comments(models.Model):
    comment = models.TextField(max_length=200)
