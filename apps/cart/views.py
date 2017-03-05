from django.shortcuts import render, get_object_or_404
from apps.cart.models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpResponse
from apps.cart.forms import ItemForm


def add_cartitem(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user, status=Cart.OPEN)
    form = ItemForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        obj = form.save(commit=False)
        obj.cart = cart
        obj.save()
        return HttpResponse(status=200)
    else:
        f = form.errors.as_data()
        print(f)
        return HttpResponse(status=410)


def change_cartitem(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user, status=Cart.OPEN)
    form = ItemForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        product = request.POST.get('product')
        quantity = request.POST.get('quantity')
        cartitem_to_change = get_object_or_404(
            CartItem, product=product, cart=cart)
        cartitem_to_change.quantity = quantity
        cartitem_to_change.save()
        return HttpResponse(status=200)
    else:
        f = form.errors.as_data()
        print(f)
        return HttpResponse(status=410)


def del_cartitem(request):
    user = request.user
    cart, created = Cart.objects.get_or_create(user=user, status=Cart.OPEN)
    if request.method == 'POST':
        cartitem_id = request.POST.get('cartitemid')
        cartitem_to_del = get_object_or_404(CartItem, id=cartitem_id)
        cartitem_to_del.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=410)


def cart(request):
    user = request.user
    try:
        cart = Cart.objects.get(user=user, status='open')
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        cart = Cart(status='open', user=user)
        cart.save()
    cartitems = CartItem.objects.filter(cart=cart)

    return render(request, 'cart.html', {'cartitems': cartitems})
