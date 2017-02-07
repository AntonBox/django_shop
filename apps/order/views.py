from django.shortcuts import render, get_object_or_404
from apps.cart.models import CartItem, Cart
from apps.order.models import Order


def order(request):
    user = request.user
    cart = get_object_or_404(Cart, user=user)
    cart_items = CartItem.objects.filter(cart=cart)
    total = 0
    for item in cart_items:
        price_for_item = item.quantity * item.product.price
        total += price_for_item
    return render(request, 'order.html', {'total': total})


def confirm(request):
    user = request.user
    cart = get_object_or_404(Cart, user=user)
    if request.is_ajax():
        adress = request.POST.get('adress')
        phone = request.POST.get('phone')
        cart.status = 'Closed'
        cart.save()
        order = Order(user=user, cart=cart, phone=phone, adress=adress)
        order.save()
    return render(request, 'confirm.html')
