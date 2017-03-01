from django.contrib import admin
from apps.core.models import Carousel


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')


admin.site.register(Carousel, CarouselAdmin)
