from django.conf.urls import url
from apps.accounts import views as account_views


urlpatterns = [
    url(r'^login/$', account_views.login_user, name='login')
]