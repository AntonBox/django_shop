from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from apps.core.decorators import cart_required

from apps.cart.models import Cart
from apps.order.forms import AddOrderForm
from apps.accounts.models import User


@ensure_csrf_cookie
@cart_required
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


@ensure_csrf_cookie
@cart_required
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
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            user = User.create_user_order(first_name, last_name, email)
            cart.user = user
            cart.save()
        obj.save()
        return render(request, 'confirm.html')
    else:
        return render(request, 'order.html', {'form': form})
