from django import forms
from .models import Order, OrderItem
from django.forms import modelformset_factory


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('id', 'customer')
