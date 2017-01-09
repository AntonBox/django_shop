from django.shortcuts import render, get_object_or_404
from apps.catalog.models import Product, Category, Carousel


def products(request, slug=None):
    products = Product.objects.all()
    categories = Category.objects.all()
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    return render(request, 'catalog.html', {'products': products,
                                            'categories': categories})


def main(request):
    visuals = Carousel.objects.order_by('index').filter(is_active=True).all()
    products = Product.objects.order_by('created_at').all()[:4]
    return render(request, 'main.html', {'visuals': visuals,
                                         'products': products})
