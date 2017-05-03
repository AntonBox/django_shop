from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.cart.models import Cart
import random
import string


class User(AbstractUser):
    def get_user_cart(self):
        cart, _ = Cart.objects.get_or_create(user=self, status=Cart.OPEN)
        return cart

    def create_user_order(first_name, last_name, email):
        username = str(last_name) + str(random.randint(1, 99))
        password = ''.join(random.choice(
            string.ascii_uppercase +
            string.ascii_lowercase + string.digits) for x in range(10))
        user = User.objects.create_user(username=username,
                                        password=password,
                                        first_name=first_name,
                                        last_name=last_name,
                                        email=email)
        return user
