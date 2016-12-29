from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import render_to_response
from apps.catalog.models import Product


class all_product1(TemplateView):

        def all_product(request):
            product = Product.objects.get(id=1)
            return render_to_response('product.html', {'product': product})
