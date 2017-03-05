from django.conf.urls import url
from apps.cart.views import cart, add_cartitem, del_cartitem, change_cartitem


urlpatterns = [
    url(r'^$', cart, name='cart'),
    url(r'^cartitem/$', add_cartitem, name='add'),
    url(r'^del/$', del_cartitem, name='del'),
    url(r'^change/$', change_cartitem, name='change')
]
