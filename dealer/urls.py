from django.urls import include, path
from rest_framework import routers

from .api_interface import DealerViewSet

router = routers.DefaultRouter()
router.register(r"dealer", DealerViewSet)
urlpatterns = [path("", include(router.urls))]
