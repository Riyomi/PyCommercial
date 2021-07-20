from django import forms
from django.db import models

from .models import Order
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

from django.core.validators import RegexValidator


class OrderForm(forms.ModelForm):
    name = forms.CharField(max_length=150, min_length=1)
    number = forms.CharField(max_length=19, min_length=19, validators=[
        RegexValidator('(\d{4} ){3}\d{4}',), ])
    expiry_date = forms.CharField(max_length=5, validators=[
                                  RegexValidator('\d\d/\d\d',), ])
    security_code = forms.CharField(
        widget=forms.PasswordInput(), max_length=3, min_length=3, validators=[RegexValidator('\d{3}',), ])

    mobile = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial="HU")
    )

    class Meta:
        model = Order
        fields = ('last_name', 'first_name', 'email',
                  'address', 'country', 'mobile', 'city')
