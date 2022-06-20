from django.urls import include, path
from rest_framework import routers

from .api_interface import ShowroomsViewSet

router = routers.DefaultRouter()
router.register(r"showroom", ShowroomsViewSet)

urlpatterns = [path("", include(router.urls))]
