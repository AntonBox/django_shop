from apps.catalog.models import Category


def menu_category(request):
    return {"category_list": Category.objects.all()}


def menu_cart(request):
    if hasattr(request, 'has_cart') and request.has_cart is True:
        menu_cart = request.cart.cartitems.count()
        return {'menu_cart': menu_cart}
    else:
        return {}
