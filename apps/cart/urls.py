from django.conf.urls import url
from apps.cart.views import cart, cartitem, del_cartitem


urlpatterns = [
    url(r'^$', cart, name='cart'),
    url(r'^cartitem/$', cartitem, name='add'),
    url(r'^del/$', del_cartitem, name='del')
]
