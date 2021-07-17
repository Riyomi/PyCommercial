from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1',
                  'password2', 'first_name', 'last_name')


class EditUserInfoForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('password', 'date_joined')


class CustomerForm(forms.ModelForm):
    mobile = PhoneNumberField(
        widget=PhoneNumberPrefixWidget(initial="HU")
    )

    class Meta:
        model = Customer
        fields = ('mobile', 'country', 'city', 'address')
