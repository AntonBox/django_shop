from django import forms
from django.forms import ModelForm
from apps.cart.models import CartItem


class ItemForm(ModelForm):
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

    def clean(self):
        cleaned_data = super(ItemForm, self).clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        if quantity > product.quantity:
            raise forms.ValidationError("Sorry")
