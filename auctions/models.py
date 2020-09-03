from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
    pass


class Auction(models.Model):
    image = models.FileField()
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.FloatField(default=0)

    def get_absolute_url(self):
        return reverse('index')


class Bids(models.Model):
    number_bids = models.IntegerField


class Comments(models.Model):
    comment = models.TextField(max_length=200)
