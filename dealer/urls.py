from django.urls import path, include
from rest_framework import routers
from .api_interface import DealerViewSet, CarViewSet

router = routers.DefaultRouter()
router.register(r'dealer', DealerViewSet)
router.register(r'car', CarViewSet)

urlpatterns = [
    path('', include(router.urls))
]
