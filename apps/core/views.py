from django.shortcuts import render
from apps.catalog.models import Product, Category
from apps.core.models import Carousel


def index(request):
    visuals = Carousel.objects.order_by('index').filter(is_active=True).all()
    products = Product.objects.order_by('created_at').all()[:4]
    categories = Category.objects.all()
    return render(request, 'main2.html', {'visuals': visuals,
                                          'products': products,
                                          'categories': categories})
