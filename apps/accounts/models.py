from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.cart.models import Cart


class User(AbstractUser):
    def get_user_cart(self):
        cart, _ = Cart.objects.get_or_create(user=self, status=Cart.OPEN)
        return cart
