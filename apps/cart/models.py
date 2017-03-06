from django.db import models
from root.base_models import TimedModel
from apps.catalog.models import Product
from django.contrib.auth.models import User


class Cart(TimedModel):
    OPEN = 'open'
    CLOSED = 'closed'
    status_choice = ((OPEN, 'Open'), (CLOSED, 'Closed'))
    user = models.ForeignKey(User)
    status = models.CharField(max_length=6,
                              choices=status_choice, default=CLOSED)

    def __str__(self):
        return self.status


class CartItem(TimedModel):
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField()
    cart = models.ForeignKey(Cart, related_name='cartitems')

    def total(self, cart):
        cart_items = self.objects.filter(cart=cart)
        total = 0
        for item in cart_items:
            price_for_item = item.quantity * item.product.price
            total += price_for_item
        return total
