from django.contrib import admin
from apps.testview import models


class VisualAdmin(admin.ModelAdmin):
    list_display = ('title', 'img')


admin.site.register(models.Visual, VisualAdmin)
