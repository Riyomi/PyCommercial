from django import forms
from django.core.validators import RegexValidator

from .models import Order
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class OrderForm(forms.ModelForm):
    name = forms.CharField(max_length=150, min_length=3)
    number = forms.CharField(max_length=19, min_length=19, validators=[
        RegexValidator('(\d{4} ){3}\d{4}',), ], error_messages={'invalid': 'Invalid credit card number'})
    expiry_date = forms.CharField(max_length=5, validators=[
                                  RegexValidator('\d\d/\d\d',), ], error_messages={'invalid': 'Invalid expiry date'})
    security_code = forms.CharField(
        widget=forms.PasswordInput(), max_length=3, min_length=3, validators=[RegexValidator('\d{3}',), ], error_messages={'invalid': 'Invalid security code'})

    mobile = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial="HU")
    )

    class Meta:
        model = Order
        fields = ('last_name', 'first_name', 'email',
                  'address', 'country', 'mobile', 'city')
