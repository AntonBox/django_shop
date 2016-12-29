from django.conf.urls import url
from apps.cart.views import karzina


urlpatterns = [
    url(r'^$', karzina.add_to_cart, name='add_to_cart'),
]
