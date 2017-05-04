from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import ensure_csrf_cookie
from apps.catalog.models import Product, Category


@ensure_csrf_cookie
def products(request, slug=None):
    products = Product.objects.all()
    categories = Category.objects.all()
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(category=category)
    return render(request, 'catalog.html', {'products': products,
                                            'categories': categories})


@ensure_csrf_cookie
def product(request, detail):
    product_for_detail = get_object_or_404(Product, detail=detail)
    return render(request, 'details.html',
                  {'product': product_for_detail})
