from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('customer.urls')),
    path('api/', include('showroom.urls')),
    path('api/', include('dealer.urls')),
    path('api/', include('transaction.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns = [path('__debug__/', include('debug_toolbar.urls')), ] + urlpatterns
