from django.shortcuts import render

from apps.cart.models import Cart
from apps.order.forms import AddOrderForm
import random
import string


def order(request):
    if request.user.is_authenticated():
        cart = request.user.get_user_cart()
    elif 'token' in request.session:
        token = request.session['token']
        cart, _ = Cart.objects.get_or_create(token=token, status=Cart.OPEN)
    else:
        token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))
        request.session['token'] = token
        cart, _ = Cart.objects.get_or_create(token=token, status=Cart.OPEN)
    total = cart.get_total()
    form = AddOrderForm()
    return render(request, 'order.html', {'total': total, 'form': form})


def confirm(request):
    if request.user.is_authenticated():
        cart = request.user.get_user_cart()
    elif 'token' in request.session:
        token = request.session['token']
        cart, _ = Cart.objects.get_or_create(token=token, status=Cart.OPEN)
    else:
        token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))
        request.session['token'] = token
        cart, _ = Cart.objects.get_or_create(token=token, status=Cart.OPEN)
    form = AddOrderForm(request.POST)
    if form.is_valid():
        cart.status = Cart.CLOSED
        cart.save()
        obj = form.save(commit=False)
        obj.cart = cart
        if request.user.is_authenticated():
            obj.user = request.user
        else:
            obj.token = token
        obj.save()
        return render(request, 'confirm.html')
    else:
        return render(request, 'order.html', {'form': form})
