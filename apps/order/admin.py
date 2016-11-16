from django.contrib import admin
from apps.order import models


class OrderAdmin(admin.ModelAdmin):
    list_display = ('phone', 'address')


admin.site.register(models.Order, OrderAdmin)


