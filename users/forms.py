from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('mobile', 'country', 'city', 'address')
