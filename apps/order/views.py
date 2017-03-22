from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from apps.core.decorators import get_cart_or_404

from apps.cart.models import Cart
from apps.order.forms import AddOrderForm


@csrf_exempt
@get_cart_or_404
def order(request):
    if request.user.is_authenticated():
        user = request.user
        cart = get_object_or_404(Cart, user=user, status=Cart.OPEN)
    else:
        token = request.session['token']
        cart = get_object_or_404(Cart, token=token, status=Cart.OPEN)
    total = cart.get_total()
    form = AddOrderForm(initial={'first_name': request.user.first_name,
                                 'last_name': request.user.last_name,
                                 'email': request.user.email})
    return render(request, 'order.html', {'total': total, 'form': form})


@csrf_exempt
@get_cart_or_404
def confirm(request):
    cart = request.cart
    form = AddOrderForm(request.POST)
    if form.is_valid():
        cart.status = Cart.CLOSED
        cart.save()
        obj = form.save(commit=False)
        obj.cart = cart
        if request.user.is_authenticated():
            obj.user = request.user
        else:
            obj.token = request.session['token']
        obj.save()
        return render(request, 'confirm.html')
    else:
        return render(request, 'order.html', {'form': form})
