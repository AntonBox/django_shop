from django.conf.urls import url
from apps.core import views as core_views

urlpatterns = [
    url(r'^$', core_views.index, name='index'),
]
