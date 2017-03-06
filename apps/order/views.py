from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from apps.cart.models import CartItem, Cart
from apps.order.forms import AddOrderForm


def order(request):
    cart = get_object_or_404(Cart, user=request.user, status=Cart.OPEN)
    total = CartItem.total(CartItem, cart)
    return render(request, 'order.html', {'total': total})


def confirm(request):
    cart = get_object_or_404(Cart, user=request.user, status=Cart.OPEN)
    form = AddOrderForm(request.POST)
    if form.is_valid():
        cart.status = 'Closed'
        cart.save()
        obj = form.save(commit=False)
        obj.cart = cart
        obj.user = request.user
        obj.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse({'message': 'Incorrect address or phone, or both!'}, status=400)
