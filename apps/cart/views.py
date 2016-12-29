
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from apps.catalog.models import Product
from django.views.decorators.csrf import csrf_protect
from apps.cart.models import Cart
from apps.cart.models import CartItem
from django.contrib.auth.models import User


@csrf_protect
class karzina:
    #    def remove_from_cart(request, product_id):
    #        product = CartItem.objects.get(product=product_id)
    #        cart = Cart(request)
    #        cart.remove(product)

    def add_to_cart(request):
        if 'quantity' in request.POST:
            quantity = request.POST['quantity']
        if 'prod' in request.POST:
            prod = request.POST['prod']
        if 'price' in request.POST:
            price = request.POST['price']
    #    cart = Cart.objects.get(quantity)
    #    if quantity < cart:
    #        print "нет товара на складе"
        cart1 = Cart(user_id=1, status='Open')
        cart1.save()
        cartim = CartItem(product_id=prod, quantity=quantity)
        cartim.save()
        try:
            order = CartItem.objects.get(product_id=prod)
        except CartItem.DoesNotExist:
            order = None
        product = Product.objects.get(id=prod)
        # проверка переменой на null и ноль
        if quantity is None and quantity is 0:
            quantity = 1
        summa = int(quantity) * float(price)
        return render_to_response('order.html', {'quantity': quantity,
        'product': product, 'price': price, 'summa': summa})
