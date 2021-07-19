from django import forms
from .models import Order, OrderItem
from django.forms import modelformset_factory
from creditcards.forms import CardNumberField, CardExpiryField, SecurityCodeField


class CustomerInfoOrderForm(forms.ModelForm):
    cc_number = CardNumberField(
        label='Card Number', required=True, max_length=19)
    cc_expiry = CardExpiryField(
        label='Expiration Date', required=True, widget=forms.TextInput(attrs={'maxlength': 5}))
    cc_code = SecurityCodeField(
        label='CVV/CVC', max_length=3, required=True, widget=forms.PasswordInput())

    class Meta:
        model = Order
        fields = ('address', 'country', 'mobile', 'city')


class UserInfoOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('last_name', 'first_name', 'email')
