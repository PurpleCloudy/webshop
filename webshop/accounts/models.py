from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    avatar = models.ImageField()
    balance = models.OneToOneField(to="Balance", on_delete=models.CASCADE)
    cart = models.OneToOneField(to="cart.Cart", on_delete=models.CASCADE)

class Balance(models.Model):
    value = models.DecimalField(decimal_places=2, max_digits=20)

class Address(models.Model):
    profile = models.ForeignKey(to="UserProfile", on_delete=models.CASCADE)
    post_index = models.CharField(max_length=9)
    country = models.CharField(max_length=40)
    region = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    street = models.CharField(max_length=40)
    house = models.CharField(max_length=10)
    apartment = models.CharField(max_length=10)