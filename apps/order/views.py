from django.shortcuts import render

from apps.cart.models import Cart
from apps.order.forms import AddOrderForm


def order(request):
    cart = request.user.get_user_cart()
    total = cart.get_total()
    form = AddOrderForm()
    return render(request, 'order.html', {'total': total, 'form': form})


def confirm(request):
    cart = request.user.get_user_cart()
    form = AddOrderForm(request.POST)
    if form.is_valid():
        cart.status = Cart.CLOSED
        cart.save()
        obj = form.save(commit=False)
        obj.cart = cart
        obj.user = request.user
        obj.save()
        return render(request, 'confirm.html')
    else:
        return render(request, 'order.html', {'form': form})
