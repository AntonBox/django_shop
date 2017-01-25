from django.contrib import admin
from apps.cart.models import Cart, CartItem


# class CartAdmin(admin.ModelAdmin):
#    list_display = ('user', 'status')


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity')


# admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
