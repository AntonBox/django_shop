from apps.cart.models import Cart
import random
import string


def get_cart(view_to_decorate):
    def cart_wrapper(request):
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
        view_to_decorate(request)
        return request
    return cart_wrapper
