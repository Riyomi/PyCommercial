from django import forms
from .models import Order, OrderItem
from django.forms import modelformset_factory


class CustomerInfoOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('address', 'country', 'mobile', 'city')


class UserInfoOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('last_name', 'first_name', 'email')
