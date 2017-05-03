from django.db import models
from root.base_models import TimedModel
from apps.catalog.models import Product
from django.conf import settings


class Cart(TimedModel):
    OPEN = 'open'
    CLOSED = 'closed'
    status_choice = ((OPEN, 'Open'), (CLOSED, 'Closed'))
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    token = models.CharField(max_length=16, blank=True, null=True)
    status = models.CharField(max_length=6,
                              choices=status_choice, default=CLOSED)

    def __str__(self):
        return self.status

    def get_total(self):
        cart_items = CartItem.objects.filter(cart=self)
        total = 0
        for item in cart_items:
            price_for_item = item.quantity * item.product.price
            total += price_for_item
        return total

    def is_permitted_for_request(self, request):
        if self.user == request.user or self.token == request.session['token']:
            return True


class CartItem(TimedModel):
    product = models.ForeignKey(Product)
    quantity = models.PositiveIntegerField()
    cart = models.ForeignKey(Cart, related_name='cartitems')

    class Meta:
        unique_together = ('product', 'cart')
