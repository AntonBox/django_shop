from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from apps.core.decorators import get_cart_or_404

from apps.cart.models import Cart
from apps.order.forms import AddOrderForm
from apps.order.functions import create_user_order


@get_cart_or_404
def order(request):
    cart = request.cart
    total = cart.get_total()
    if request.user.is_authenticated():
        form = AddOrderForm(initial={'first_name': request.user.first_name,
                                     'last_name': request.user.last_name,
                                     'email': request.user.email})
    else:
        form = AddOrderForm()
    return render(request, 'order.html', {'total': total, 'form': form})


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
            last_name = form.fields['last_name']
            user = create_user_order(last_name)
            obj.user = user
            cart.user = user
            cart.save()
        obj.save()
        return render(request, 'confirm.html')
    else:
        return render(request, 'order.html', {'form': form})
