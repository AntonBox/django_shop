from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from apps.core.models import Carousel
from apps.catalog.models import Product, Category


@ensure_csrf_cookie
def index(request):
    visuals = Carousel.objects.order_by('index').filter(is_active=True).all()
    products = Product.objects.order_by('created_at').all()[:4]
    categories = Category.objects.all()
    return render(request, 'main.html', {'visuals': visuals,
                                         'products': products,
                                         'categories': categories})
