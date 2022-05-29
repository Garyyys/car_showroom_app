from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('customer.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    # path('api/', include('showroom.urls')),
    # path('api/', include('dealer.urls')),
    # path('api/', include('dealer.urls')),
]

if settings.DEBUG:
    urlpatterns = [path('__debug__/', include('debug_toolbar.urls')), ] + urlpatterns
