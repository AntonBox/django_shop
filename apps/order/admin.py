from django.contrib import admin
from apps.order import models


class OrderAdmin(admin.ModelAdmin):
    list_display = ('phone', 'adress')


admin.site.register(models.Order, OrderAdmin)
