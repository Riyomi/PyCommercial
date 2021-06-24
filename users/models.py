from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False
User._meta.get_field('first_name').blank = False
User._meta.get_field('first_name').null = False
User._meta.get_field('last_name').blank = False
User._meta.get_field('last_name').null = False


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mobile = PhoneNumberField()
    country = models.CharField('Country', max_length=50)
    city = models.CharField('City', max_length=30)
    address = models.CharField('Address', max_length=50)

    def __str__(self):
        return self.user.email
