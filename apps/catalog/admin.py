from django.contrib import admin
from apps.catalog.models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
