from django.shortcuts import render_to_response
from apps.catalog.models import Product


def catalog(request):
    products = Product.objects.order_by('price').all()
    return render_to_response('catalog.html', {'products': products})
