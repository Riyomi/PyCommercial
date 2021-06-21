from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mobile = models.CharField('Mobile number', max_length=20)
    country = models.CharField('Country', max_length=50)
    city = models.CharField('City', max_length=30)
    address = models.CharField('Address', max_length=50)

    def __str__(self):
        return self.user.email
