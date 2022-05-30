from django.urls import path, include
from rest_framework import routers
from .api_interface import ShowroomsViewSet

router = routers.DefaultRouter()
router.register(r'showroom', ShowroomsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
