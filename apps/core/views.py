from django.shortcuts import render
from apps.catalog.models import Product
from apps.core.models import Carousel


def index(request):
    visuals = Carousel.objects.order_by('index').filter(is_active=True).all()
    products = Product.objects.order_by('created_at').all()[:4]
    return render(request, 'main.html', {'visuals': visuals,
                                         'products': products})
