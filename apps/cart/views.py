from django.shortcuts import render, get_object_or_404
from apps.catalog.models import Product
from apps.cart.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def cart(request):
    user = request.user
    try:
        cart = Cart.objects.get(user=user, status='Open')
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        cart = Cart(status='Open', user=user)
        cart.save()

    if request.is_ajax():
        # add product to cart
        if 'productid' in request.POST:
            product_id = request.POST.get('productid')
            product_to_cart = get_object_or_404(Product, id=product_id)
            cartitem = CartItem(product=product_to_cart, quantity=1, cart=cart)
            cartitem.save()
        # delete product from cart
        if 'cartitemid' in request.POST:
            cartitem_id = request.POST.get('cartitemid')
            cartitem_to_del = get_object_or_404(CartItem, id=cartitem_id)
            cartitem_to_del.delete()
        # change produt`s quantity
        if 'quantity' in request.POST:
            cartitem_id = request.POST.get('cartitem')
            quantity = request.POST.get('quantity')
            cartitem_to_change = get_object_or_404(CartItem, id=cartitem_id)
            cartitem_to_change.quantity = quantity
            cartitem_to_change.save()

    cartitems = CartItem.objects.filter(cart=cart)

    return render(request, 'cart.html', {'cartitems': cartitems})
