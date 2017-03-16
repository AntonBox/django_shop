from django.conf.urls import url
from apps.order import views as order_views

urlpatterns = [
    url(r'^$', order_views.order, name='order'),
    url(r'^confirm/$', order_views.confirm, name='confirm'),
]
