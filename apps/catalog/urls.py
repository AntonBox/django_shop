from django.conf.urls import url
from apps.catalog.views import catalog

urlpatterns = [
    url(r'^$', catalog, name='catalog')
]
