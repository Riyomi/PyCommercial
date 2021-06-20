from django.db import models
from django import forms


class Customer(models.Model):
    email = models.EmailField('Email')
    password = models.CharField(widget=forms.PasswordInput, max_length=30)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
