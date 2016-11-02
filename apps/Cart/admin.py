from django.contrib import admin
from apps.Cart.models import User, Cart, CartItem

admin.site.register(User)
admin.site.register(Cart)
admin.site.register(CartItem)
