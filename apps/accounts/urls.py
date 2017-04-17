from django.conf.urls import url
from apps.accounts import views as account_views


urlpatterns = [
    url(r'^registration/$', account_views.registration, name='registration')
]