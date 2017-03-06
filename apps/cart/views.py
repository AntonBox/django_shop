from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from apps.cart.forms import EditItemForm, AddItemForm
from apps.cart.models import Cart, CartItem


def add_cartitem(request):
    cart, _ = Cart.objects.get_or_create(user=request.user, status=Cart.OPEN)
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
    if cartitem.cart.user == request.user:
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
    if cartitem.cart.user == request.user:
        cartitem.delete()
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=403)
