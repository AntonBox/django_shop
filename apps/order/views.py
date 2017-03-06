from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from apps.cart.models import CartItem, Cart
from apps.order.forms import AddOrderForm


def order(request):
    cart = Cart.get_user_cart_or_404(request.user)
    total = cart.get_total()
    return render(request, 'order.html', {'total': total})


def confirm(request):
    cart = Cart.get_user_cart_or_404(request.user)
    form = AddOrderForm(request.POST)
    if form.is_valid():
        cart.status = 'Closed'
        cart.save()
        obj = form.save(commit=False)
        obj.cart = cart
        obj.user = request.user
        obj.save()
        return redirect('/deal/')
    else:
        return HttpResponse({'message': 'Incorrect address or phone, or both!'}, status=400)
