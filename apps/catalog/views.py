from django.shortcuts import render_to_response, get_object_or_404
from apps.catalog.models import Product, Category


def catalog(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render_to_response('catalog.html', {
        'products': products,
        'categories': categories
    })


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('catalog.html', {
        'category': category,
        'products': Product.objects.filter(category=category)
    })
