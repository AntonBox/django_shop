from django.conf.urls import url
from apps.testview.views import TestView

urlpatterns = [
    url(r'^$', TestView.as_view(), name='testview'),
]
