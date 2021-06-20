from django.db import models


class Customer(models.Model):
    email = models.EmailField('Email')
    password = models.CharField('Password', max_length=30)
    name = models.CharField('Full name', max_length=100)
    mobile = models.CharField('Mobile number', max_length=20)
    country = models.CharField('Country', max_length=50)
    city = models.CharField('City', max_length=30)
    address = models.CharField('Address', max_length=50)

    def __str__(self):
        return self.email
