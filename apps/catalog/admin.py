from django.contrib import admin
from apps.catalog.models import Category, Product



class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','description')


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
