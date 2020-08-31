from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction(models.Model):
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    price = models.FloatField


class Bids(models.Model):
    number_bids = models.IntegerField


class Comments(models.Model):
    comment = models.TextField(max_length=200)
