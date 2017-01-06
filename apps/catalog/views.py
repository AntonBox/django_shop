from django.shortcuts import render, get_object_or_404
from apps.catalog.models import Product, Category

'''
def catalog(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, 'catalog.html', {
        'products': products,
        'categories': categories
    })


def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render(request, 'catalog.html', {
        'categories': Category.objects.all(),
        'products': Product.objects.filter(category=category)
    })
'''

'''
def products(request, slug=None):
    if (slug is not None):
        category = get_object_or_404(Category, slug=slug)
        return render(request, 'catalog.html', {
            'categories': Category.objects.all(),
            'products': Product.objects.filter(category=category)
        })
    else:
        products = Product.objects.all()
        categories = Category.objects.all()
        return render(request, 'catalog.html', {
            'products': products,
            'categories': categories
        })
'''


def products(request, slug=None):
    products = Product.objects.all()
    categories = Category.objects.all()
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = Product.objects.filter(category=category)
    return render(request, 'catalog.html', {'products': products,
                                            'categories': categories})
