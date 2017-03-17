from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from apps.cart.forms import EditItemForm, AddItemForm
from apps.cart.models import CartItem, Cart
import random
import string


def cart(request):
    if request.user.is_authenticated():
        cart = request.user.get_user_cart()
    elif 'token' in request.session:
        token = request.session['token']
        cart, _ = Cart.objects.get_or_create(token=token, status=Cart.OPEN)
    else:
        token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))
        request.session['token'] = token
        cart, _ = Cart.objects.get_or_create(token=token, status=Cart.OPEN)
    cartitems = cart.cartitems.all()
    return render(request, 'cart.html', {'cartitems': cartitems})


def add_cartitem(request):
    if request.user.is_authenticated():
        cart = request.user.get_user_cart()
    elif 'token' in request.session:
        token = request.session['token']
        cart, _ = Cart.objects.get_or_create(token=token, status=Cart.OPEN)
    else:
        token = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for x in range(16))
        request.session['token'] = token
        cart, _ = Cart.objects.get_or_create(token=token, status=Cart.OPEN)
    form = AddItemForm(request.POST, cart=cart)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.cart = cart
        obj.save()
        return HttpResponse(status=200)
    else:
        return HttpResponse({'message': 'Sample error message!'}, status=400)


def change_cartitem(request):
    cartitem_id = request.POST.get('cartitemid')
    cartitem = get_object_or_404(CartItem, id=cartitem_id)
    if cartitem.cart.user == request.user or cartitem.cart.token == request.session['token']:
        form = EditItemForm(request.POST, instance=cartitem)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)
    else:
        return HttpResponse(status=403)


def del_cartitem(request):
    cartitem_id = request.POST.get('cartitemid')
    cartitem = get_object_or_404(CartItem, id=cartitem_id)
    if cartitem.cart.user == request.user or cartitem.cart.token == request.session['token']:
        cartitem.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=403)
