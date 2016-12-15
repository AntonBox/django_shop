from django.conf.urls import url
from apps.catalog.views import catalog, view_category

urlpatterns = [
    url(r'^$', catalog),
    url(r'^category/(?P<slug>[^\.]+).html',
        view_category, name='view_category_url'),
]
