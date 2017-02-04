from django.conf.urls import url
from apps.catalog import views as catalog_views

urlpatterns = [
    url(r'^catalog/$', catalog_views.products, name='catalog'),
    url(r'^catalog/category/(?P<slug>[-\w]+)$',
        catalog_views.products, name='view_category'),
    url(r'^$', catalog_views.index)
]
