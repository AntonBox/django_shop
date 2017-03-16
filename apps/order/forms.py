from django.forms import ModelForm

from apps.order.models import Order


class AddOrderForm(ModelForm):

    class Meta:
        model = Order
        fields = ['phone', 'address']
