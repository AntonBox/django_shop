from django import forms
from django.forms import ModelForm

from apps.cart.models import CartItem


class AddItemForm(ModelForm):

    class Meta:
        model = CartItem
        fields = ['product', 'quantity']

    def __init__(self, *args, **kwargs):
        self.cart = kwargs.pop('cart')
        super(AddItemForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(AddItemForm, self).clean()
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        if quantity > product.quantity:
            raise forms.ValidationError("Sorry")

        if CartItem.objects.filter(cart=self.cart, product=product).exists():
            raise forms.ValidationError("Already in cart!")


class EditItemForm(ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']

    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        if quantity > self.instance.product.quantity:
            raise forms.ValidationError("Sorry")

        return quantity
