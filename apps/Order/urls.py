from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.TestView.as_view(), name='test_template')
]
