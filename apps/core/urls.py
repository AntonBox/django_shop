from django.conf.urls import url
from apps.core import views as core_views

urlpatterns = [
    url(r'^$', core_views.index, name='index'),
    url(r'^deal/$', core_views.deal, name='deal')
]
