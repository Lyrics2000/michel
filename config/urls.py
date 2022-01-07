
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('account.urls',namespace="account")),
    path('farmers/',include('farmers.urls',namespace="farmers")),
    path('vendors/',include('vendors.urls',namespace="vendors")),
    path('customers/',include('customers.urls',namespace="customers"))
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

