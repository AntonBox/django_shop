from django.conf.urls import url
from apps.testview.views import TestView
from apps.testview.views import vision

urlpatterns = [
    url(r'^caro/$', vision, name='vision'),
    url(r'^$', TestView.as_view(), name='testview'),
]
