from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from apps.cart.forms import EditItemForm, AddItemForm
from apps.cart.models import CartItem
from apps.core.decorators import get_cart


@csrf_exempt
@get_cart
def cart(request):
    cart = request.cart
    cartitems = cart.cartitems.all()
    return render(request, 'cart.html', {'cartitems': cartitems})


@csrf_exempt
@get_cart
def add_cartitem(request):
    cart = request.cart
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
