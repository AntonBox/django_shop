from django.db import models
from root.base_models import TimedModel
from apps.cart.models import Cart
from django.conf import settings


class Order(TimedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    cart = models.ForeignKey(Cart, blank=True, null=True, on_delete=models.SET_NULL)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
