from django.contrib import admin
from apps.catalog.models import Category, Product, Carousel


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Carousel, CarouselAdmin)
