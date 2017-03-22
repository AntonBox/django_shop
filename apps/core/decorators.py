from apps.cart.models import Cart
from django.shortcuts import get_object_or_404
import random
import string


def get_cart(the_func):
    def _decorated(request, *args, **kwargs):
        if request.user.is_authenticated():
            cart = request.user.get_user_cart()
        elif 'token' in request.session:
            token = request.session['token']
            cart, _ = Cart.objects.get_or_create(token=token, status=Cart.OPEN)
        else:
            token = ''.join(random.choice(
                string.ascii_uppercase +
                string.ascii_lowercase + string.digits) for x in range(16))
            request.session['token'] = token
            cart, _ = Cart.objects.get_or_create(token=token, status=Cart.OPEN)
        request.cart = cart
        return the_func(request, *args, **kwargs)
    return _decorated


def get_cart_or_404(the_func):
    def _decorated(request, *args, **kwargs):
        if request.user.is_authenticated():
            user = request.user
            cart = get_object_or_404(Cart, user=user, status=Cart.OPEN)
        else:
            token = request.session['token']
            cart = get_object_or_404(Cart, token=token, status=Cart.OPEN)
        request.cart = cart
        return the_func(request, *args, **kwargs)
    return _decorated
