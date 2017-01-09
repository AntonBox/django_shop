from django.conf.urls import url
from apps.catalog import views as catalog_views

urlpatterns = [
    url(r'^$', catalog_views.products, name='catalog'),
    url(r'^category/(?P<slug>[-\w]+)$',
        catalog_views.products, name='view_category'),
    url(r'^main$', catalog_views.main)
]
