from django.contrib import admin
from apps.Catalog.models import Category, Product


admin.site.register(Category)
admin.site.register(Product)
