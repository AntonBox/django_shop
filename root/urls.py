from django.contrib import admin
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^btemp/', include('apps.testview.urls')),
    url(r'^catalog/', include('apps.catalog.urls')),
    url(r'^cart/', include('apps.cart.urls')),
    url(r'^', include('apps.core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
