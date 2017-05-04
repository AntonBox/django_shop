from django import forms
from django.forms import ModelForm

from apps.order.models import Order
from apps.cart.models import Cart


class AddOrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address']

    def clean_cart(self):
        cart = self.cleaned_data['cart']
        if cart.status != Cart.OPEN:
            raise forms.ValidationError("Cart is already closed")

        return cart
