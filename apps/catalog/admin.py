from django.contrib import admin
from apps.catalog.models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')
    prepopulated_fields = {'detail': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
