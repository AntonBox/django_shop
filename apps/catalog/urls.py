from django.conf.urls import url
from apps.catalog.views import all_product1

#urlpatterns = [
#    url(r'^$', all_product1.as_view(), name='all_product'),
#]

#from django.conf.urls import url
#from apps.testview.views import TestView

urlpatterns = [
    url(r'^$', all_product1.all_product, name='all_product'),

]
