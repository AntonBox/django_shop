from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.order.forms import AddOrderForm


def order(request):
    cart = request.user.get_user_cart()
    total = cart.get_total()
    return render(request, 'order.html', {'total': total})


def confirm(request):
    cart = request.user.get_user_cart()
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
