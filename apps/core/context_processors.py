from django.shortcuts import get_object_or_404
from apps.catalog.models import Category
from apps.cart.models import Cart
from django.http import Http404


def menu_category(request):
    category_list = Category.objects.all()
    return {"category_list": category_list}


def menu_cart(request):
    try:
        if request.user.is_authenticated():
            user = request.user
            cart = get_object_or_404(Cart, user=user, status=Cart.OPEN)
        else:
            token = request.session['token']
            cart = get_object_or_404(Cart, token=token, status=Cart.OPEN)
        total = cart.get_quantity()
        if total > 0:
            return {"total_menu": total}
        else:
            return {}
    except Http404:
        return {}
