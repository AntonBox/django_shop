from django.utils.deprecation import MiddlewareMixin
from apps.cart.models import Cart
import random
import string
from django.utils.functional import SimpleLazyObject


class CartMiddleware(MiddlewareMixin):
    def process_request(self, request):
        def create_cart():
            if request.user.is_authenticated():
                user = request.user
                cart = Cart.objects.create(user=user, status=Cart.OPEN)
            else:
                token = ''.join(random.choice(
                                string.ascii_uppercase +
                                string.ascii_lowercase +
                                string.digits) for x in range(16))
                request.session['token'] = token
                cart = Cart.objects.create(token=token, status=Cart.OPEN)
            return cart
        if request.user.is_authenticated():
            user = request.user
            check_cart = Cart.objects.filter(user=user,
                                             status=Cart.OPEN).exists()
            if check_cart is True:
                request.cart = Cart.objects.get(user=user, status=Cart.OPEN)
            else:
                request.cart = SimpleLazyObject(create_cart)
            request.has_cart = True
        elif 'token' in request.session:
            token = request.session['token']
            check_cart = Cart.objects.filter(token=token,
                                             status=Cart.OPEN).exists()
            if check_cart is True:
                request.cart = Cart.objects.get(token=token,
                                                status=Cart.OPEN)
                request.has_cart = True
            else:
                request.cart = SimpleLazyObject(create_cart)
            request.has_cart = True
        else:
            request.cart = SimpleLazyObject(create_cart)
            request.has_cart = False
        return None
